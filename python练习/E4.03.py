n,m,a,b=eval(input().replace(' ',','))
x1=n*a
x2=(n//m+1)*b
x3=(n-n%m)*a+b
x4=n//m*b+n%m*a
if x1<=x2:
    min=x1
else:
    min=x2
if x3<min:
    min=x3
if x4<min:
    min=x4
print(x4)
