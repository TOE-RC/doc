//该文件只包含一个表示数学公式的函数
//该函数用于求足端的运动学逆解
void inverseKinematics(){
  float alpha1,alpha2,beta1,beta2;
  //uint16_t servoLeftFront,servoLeftRear,servoRightFront,servoRightRear;//这是定义转动的，转化成c就是下面这条
  unsigned short servoLeftFront,servoLeftRear,servoRightFront,servoRightRear;
//这一步是代换简化用的a,b,c,d,e,f,x,y
  float aLeft = 2 * IKParam.XLeft * L1;
  float bLeft = 2 * IKParam.YLeft * L1;
  float cLeft = IKParam.XLeft * IKParam.XLeft + IKParam.YLeft * IKParam.YLeft + L1 * L1 - L2 * L2;
  float dLeft = 2 * L4 * IKParam.XLeft;
  float eLeft = 2 * L4 * IKParam.YLeft;
  float fLeft = (IKParam.XLeft * IKParam.XLeft + L4 * L4 + IKParam.YLeft * IKParam.YLeft - L3 * L3);

//这一步a1,a2是阿尔法解，b1,b2是贝塔解
  alpha1 = 2 * atan((bLeft + sqrt((aLeft * aLeft) + (bLeft * bLeft) - (cLeft * cLeft))) / (aLeft + cLeft));
  alpha2 = 2 * atan((bLeft - sqrt((aLeft * aLeft) + (bLeft * bLeft) - (cLeft * cLeft))) / (aLeft + cLeft));
  beta1 = 2 * atan((eLeft + sqrt((dLeft * dLeft) + eLeft * eLeft - (fLeft * fLeft))) / (dLeft + fLeft));
  beta2 = 2 * atan((eLeft - sqrt((dLeft * dLeft) + eLeft * eLeft - (fLeft * fLeft))) / (dLeft + fLeft));

//转化阿尔法的角度为正的
  alpha1 = (alpha1 >= 0)?alpha1:(alpha1 + 2 * PI);
  alpha2 = (alpha2 >= 0)?alpha2:(alpha2 + 2 * PI);

//取大取小
  if(alpha1 >= PI/4) IKParam.alphaLeft = alpha1;
  else IKParam.alphaLeft = alpha2;
  if(beta1 >= 0 && beta1 <= PI/4) IKParam.betaLeft = beta1;
  else IKParam.betaLeft = beta2;
  
//右边代换
  float aRight = 2 * IKParam.XRight * L1;
  float bRight = 2 * IKParam.YRight * L1;
  float cRight = IKParam.XRight * IKParam.XRight + IKParam.YRight * IKParam.YRight + L1 * L1 - L2 * L2;
  float dRight = 2 * L4 * IKParam.XRight;
  float eRight = 2 * L4 * IKParam.YRight;
  float fRight = (IKParam.XRight * IKParam.XRight+ L4 * L4 + IKParam.YRight * IKParam.YRight - L3 * L3);

//右边的两个解
  IKParam.alphaRight = 2 * atan((bRight + sqrt((aRight * aRight) + (bRight * bRight) - (cRight * cRight))) / (aRight + cRight));
  IKParam.betaRight = 2 * atan((eRight - sqrt((dRight * dRight) + eRight * eRight - (fRight * fRight))) / (dRight + fRight));

//右边解
  alpha1 = 2 * atan((bRight + sqrt((aRight * aRight) + (bRight * bRight) - (cRight * cRight))) / (aRight + cRight));
  alpha2 = 2 * atan((bRight - sqrt((aRight * aRight) + (bRight * bRight) - (cRight * cRight))) / (aRight + cRight));
  beta1 = 2 * atan((eRight + sqrt((dRight * dRight) + eRight * eRight - (fRight * fRight))) / (dRight + fRight));
  beta2 = 2 * atan((eRight - sqrt((dRight * dRight) + eRight * eRight - (fRight * fRight))) / (dRight + fRight));

//右边正角度重写
  alpha1 = (alpha1 >= 0)?alpha1:(alpha1 + 2 * PI);
  alpha2 = (alpha2 >= 0)?alpha2:(alpha2 + 2 * PI);

//右边取大取小重写
  if(alpha1 >= PI/4) IKParam.alphaRight = alpha1;
  else IKParam.alphaRight = alpha2;
  if(beta1 >= 0 && beta1 <= PI/4) IKParam.betaRight = beta1;
  else IKParam.betaRight = beta2;
//左
  alphaLeftToAngle = (int)((IKParam.alphaLeft / 6.28) * 360);//弧度转角度
  betaLeftToAngle = (int)((IKParam.betaLeft / 6.28) * 360);
//右
  alphaRightToAngle = (int)((IKParam.alphaRight / 6.28) * 360);
  betaRightToAngle = (int)((IKParam.betaRight / 6.28) * 360);
//疑似调参特异性？
  servoLeftFront = 90 + betaLeftToAngle;
  servoLeftRear = 90 + alphaLeftToAngle;
  servoRightFront = 270 - betaRightToAngle;
  servoRightRear = 270 - alphaRightToAngle;

  setServoAngle(servoLeftFront,servoLeftRear,servoRightFront,servoRightRear);
}

//以下是上面未定义的说明
//L1,L2,L3,L4分别:1,4是大腿长度，23是小腿长度
//atan()是'arctan()',sqrt()是'根号下()'




//该类型定义是在头文件的，现在放在这里方便理解
typedef struct{
    float alphaLeft, betaLeft;
    float alphaRight, betaRight;
    float XLeft,YLeft;
    float XRight, YRight;
}IKparam;


 unsigned short alphaLeftToAngle,betaLeftToAngle,alphaRightToAngle,betaRightToAngle;


