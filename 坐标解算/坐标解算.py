import cv2
import numpy as np

# 全局变量，用于记录鼠标拖动时的状态和节点位置
drawing = False
ix, iy = -1, -1
node_x, node_y = 100, 100  # 初始足端节点位置

# 固定点坐标（置于屏幕中央）
fixed_point_x, fixed_point_y = 250, 250  

# 大腿和小腿长度（示例长度，可按需修改）
thigh_length = 50
shin_length = 80

# 鼠标回调函数，用于处理鼠标事件（这里主要是鼠标按下、移动、松开时对节点位置的更新）
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, node_x, node_y
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            node_x = x
            node_y = y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


# 计算两圆交点（即关节坐标）的函数，返回两个交点坐标的列表
def calculate_intersection(circle1_center, circle1_radius, circle2_center, circle2_radius):
    """
    计算两圆交点坐标

    参数:
    circle1_center: 第一个圆的圆心坐标 (x, y)
    circle1_radius: 第一个圆的半径
    circle2_center: 第二个圆的圆心坐标 (x, y)
    circle2_radius: 第二个圆的半径

    返回值:
    intersections: 包含两个交点坐标的列表，格式为 [(x1, y1), (x2, y2)]，若不存在交点则返回空列表
    """
    x1, y1 = circle1_center
    r1 = circle1_radius
    x2, y2 = circle2_center
    r2 = circle2_radius

    d = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # 两圆不相交的情况判断
    if d > r1 + r2 or d < abs(r1 - r2):
        return []

    a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    h = np.sqrt(r1 ** 2 - a ** 2)

    xm = x1 + a * (x2 - x1) / d
    ym = y1 + a * (y2 - y1) / d

    x3 = int(xm + h * (y2 - y1) / d)
    y3 = int(ym - h * (x2 - x1) / d)
    x4 = int(xm - h * (y2 - y1) / d)
    y4 = int(ym + h * (x2 - x1) / d)

    return [(x3, y3), (x4, y4)]


# 创建一个黑色背景的图像
img = np.zeros((500, 500, 3), np.uint8)

# 创建窗口并设置鼠标回调函数
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    # 清空图像
    img = np.zeros((500, 500, 3), np.uint8)  

    # 绘制坐标系（白色线条，x向上，y向右）
    cv2.line(img, (fixed_point_x, 0), (fixed_point_x, 500), (255, 255, 255), 1)  # x轴（向上）
    cv2.line(img, (0, fixed_point_y), (500, fixed_point_y), (255, 255, 255), 1)  # y轴（向右）

    # 绘制固定点（用蓝色圆形表示）
    cv2.circle(img, (fixed_point_x, fixed_point_y), 10, (255, 0, 0), -1)  

    # 以固定点为圆心，大腿长度为半径画圆（仅示意，实际可不绘制这个圆）
    # cv2.circle(img, (fixed_point_x, fixed_point_y), thigh_length, (255, 255, 255), 1)  

    # 以足端为圆心，小腿长度为半径画圆（仅示意，实际可不绘制这个圆）
    # cv2.circle(img, (node_x, node_y), shin_length, (255, 255, 255), 1)  

    # 计算两圆交点（关节坐标）
    intersections = calculate_intersection((fixed_point_x, fixed_point_y), thigh_length, (node_x, node_y), shin_length)
    if len(intersections) == 2:
        joint1_x, joint1_y = intersections[0]
        joint2_x, joint2_y = intersections[1]

        # 计算大腿与y轴所成角度（使用简单三角函数关系，角度以度为单位）
        angle1 = np.degrees(np.arctan2(joint1_y - fixed_point_y, joint1_x - fixed_point_x))
        angle2 = np.degrees(np.arctan2(joint2_y - fixed_point_y, joint2_x - fixed_point_x))

        # 绘制大腿（用绿色线条表示）
        cv2.line(img, (fixed_point_x, fixed_point_y), (joint1_x, joint1_y), (0, 255, 0), 2)
        cv2.line(img, (fixed_point_x, fixed_point_y), (joint2_x, joint2_y), (0, 255, 0), 2)

        # 绘制小腿（用黄色线条表示）
        cv2.line(img, (joint1_x, joint1_y), (node_x, node_y), (0, 255, 255), 2)
        cv2.line(img, (joint2_x, joint2_y), (node_x, node_y), (0, 255, 255), 2)

        # 绘制足端节点（用红色圆形表示）
        cv2.circle(img, (node_x, node_y), 10, (0, 0, 255), -1)  

        # 标注大腿与y轴所成角度（文本显示，设置合适的字体、大小、颜色等）
        cv2.putText(img, f"Angle1: {angle1:.2f}", (joint1_x + 5, joint1_y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(img, f"Angle2: {angle2:.2f}", (joint2_x + 5, joint2_y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # 标注足端关于坐标系原点（固定点）的坐标（文本显示）
        cv2.putText(img, f"(X,Y): ({node_x - fixed_point_x:.2f}, {node_y - fixed_point_y:.2f})", (node_x + 5, node_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)


    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # 按下ESC键退出
        break

cv2.destroyAllWindows()