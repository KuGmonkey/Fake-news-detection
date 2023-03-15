from math import sqrt,acos,degrees
x1,y1,x2,y2,x3,y3=eval(input())
a=sqrt((x1-x2)**2+(y1-y2)**2)
b=sqrt((x1-x3)**2+(y1-y3)**2)
c=sqrt((x3-x2)**2+(y3-y2)**2)

A=degrees(acos((b*b+c*c-a*a)/(2*b*c)))
B=degrees(acos((a*a+c*c-b*b)/(2*a*c)))
C=degrees(acos((b*b+a*a-c*c)/(2*b*a)))

print('%.2f,%.2f,%.2f'%(A,B,C))
