a=eval(input())
b=a//3600
c=a%3600//60
d=a%3600%60
print('%02d:%02d:%02d'%(b,c,d))
