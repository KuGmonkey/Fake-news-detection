n=eval(input())
d={}
m=0
for i in range(n):
    a=input().split()
    try:
        d[a[0]]
        d[a[0]]+=int(a[1])
    except:
        d[a[0]]=int(a[1])
    if d[a[0]]>m:
        m=d[a[0]]
        w=a[0]
print(w)
