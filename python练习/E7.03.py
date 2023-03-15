n=eval(input())
a=eval(input().replace(' ',','))
p=0
q=0
for i in range(n):
    if a[i]>0:
        p+=a[i]
    else:
        if p==0:
            q+=1
        else:
            p-=1
print(q)
