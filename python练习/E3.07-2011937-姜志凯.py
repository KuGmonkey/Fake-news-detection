r,y,l=eval(input())
m=r*0.01/12
x=(1+m)**(12*y)
yue=l*m/(1-1/x)
zong=yue*12*y
print('%.2f'%yue)
print('%.2f'%zong)
