n=eval(input())
if n>=0:
    print(n)
else:
    n=-n
    x1=n//10
    x2=n//100*10+n%10
    print(-min(x1,x2))
