y=eval(input())
d=[]
for i in range(y):
    l=[]
    c=0
    n=eval(input())
    for k in range(n):
        l.append(set(input()))
    x=l[0]
    for j in l:
        x=x.intersection(j)
    d.append(len(x))
for p in range(y):
    print(d[p])
