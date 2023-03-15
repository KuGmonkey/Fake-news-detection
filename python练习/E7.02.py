n=eval(input())
a=list(map(int,list(input())))
b=list(map(int,list(input())))
s=0
for i in range(n):
    m=a[i]-b[i]
    if abs(m)>5:
        s+=10-abs(m)
    else:
        s+=abs(m)
print(s)
