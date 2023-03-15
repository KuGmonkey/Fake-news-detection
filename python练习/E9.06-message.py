n=eval(input())
for i in range(n):
    m=eval(input())
    l=list(input())
    for j in range(0,m,2):
        if j+1<m:
            l[j],l[j+1]=l[j+1],l[j]
    for k in range(m):
        l[k]=chr(219-ord(l[k]))
    s1=''.join(l)
    print(s1)
