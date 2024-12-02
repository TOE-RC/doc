插入串口设备后,USB可以正常发现设备`Bus 003 Device 016`但是`ls /dev`中却找不到串口设备

```bash
rick@rick:~$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 002 Device 002: ID 0bda:9210 Realtek Semiconductor Corp. RTL9210 M.2 NVME Adapter
Bus 002 Device 006: ID 2717:5006 Xiaomi Inc. 4-Port USB 3.0 Hub
Bus 002 Device 007: ID 0bda:8153 Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
Bus 002 Device 008: ID 0bda:0412 Realtek Semiconductor Corp. 4-Port USB 3.0 Hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 002: ID 1a40:0101 Terminus Technology Inc. Hub
Bus 003 Device 003: ID 30c9:0041 Luxvisions Innotech Limited USB Camera
Bus 003 Device 004: ID 258a:015e BY Tech Gaming Keyboard
Bus 003 Device 005: ID 8087:0033 Intel Corp. AX211 Bluetooth
Bus 003 Device 006: ID 1ea7:0066 SHARKOON Technologies GmbH [Mediatrack Edge Mini Keyboard]
Bus 003 Device 010: ID 2717:5007 Xiaomi Inc. 4-Port USB 2.0 Hub
Bus 003 Device 011: ID 0bda:5412 Realtek Semiconductor Corp. 4-Port USB 2.0 Hub
Bus 003 Device 016: ID 1a86:7523 QinHeng Electronics CH340 serial converter
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

```

查看日志发现串口设备被`brltty`软件占有

```bash
rick@rick:~$ sudo dmesg | grep ttyS*
[    0.069611] printk: legacy console [tty0] enabled
[    1.860154] dw-apb-uart.5: ttyS4 at MMIO 0x4017005000 (irq = 16, base_baud = 6250000) is a 16550A
[ 2199.932595] usb 3-3.4: ch341-uart converter now attached to ttyUSB0
[ 2200.584625] usb 3-3.4: usbfs: interface 0 claimed by ch341 while 'brltty' sets config #1
[ 2200.585977] ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0
[ 3316.829408] usb 3-3.4: ch341-uart converter now attached to ttyUSB0
[ 3317.481054] usb 3-3.4: usbfs: interface 0 claimed by ch341 while 'brltty' sets config #1
[ 3317.482143] ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0
[ 3387.491640] usb 3-3.4: ch341-uart converter now attached to ttyUSB0
[ 3388.144108] usb 3-3.4: usbfs: interface 0 claimed by ch341 while 'brltty' sets config #1
[ 3388.145187] ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0
[ 3483.489215] usb 3-3.4: ch341-uart converter now attached to ttyUSB0
[ 3484.149430] usb 3-3.4: usbfs: interface 0 claimed by ch341 while 'brltty' sets config #1
[ 3484.150483] ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0
[ 4280.418100] usb 3-3.4: ch341-uart converter now attached to ttyUSB0
[ 4281.080859] usb 3-3.4: usbfs: interface 0 claimed by ch341 while 'brltty' sets config #1
[ 4281.081944] ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0
```

* `dw-apb-uart.5: ttyS4 at MMIO 0x4017005000 (irq = 16, base_baud = 6250000) is a 16550A`：这是关于系统板上的一个串口（ttyS4）的信息，与您的USB串口转换器无关。
* `usb 3-3.4: ch341-uart converter now attached to ttyUSB0`：这条消息表明CH340串口转换器被连接到了`ttyUSB0`。
* `usb 3-3.4: usbfs: interface 0 claimed by ch341 while 'brltty' sets config #1`：这条消息表明`brltty`（一个用于盲人和视觉障碍人士的软件）正在尝试使用CH340设备。
* `ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0`：这条消息表明CH340串口转换器从`ttyUSB0`断开了连接。

1. 停止 `brltty` 服务：

```
sudo systemctl stop brltty
```

2. 禁止 `brltty` 自动启动：

```
sudo systemctl disable brltty
```

3. 卸载 `brltty` 软件包：

```
sudo apt remove brltty
```

4. 清理相关的配置文件和依赖项：

```
sudo apt autoremove