n=int(input())
a=list(map(int,input().split()))
x=a.index(min(a))
y=a.index(max(a))
if y<x:
    print(y+n-1-x)
else:
    print(y+n-1-x-1)
