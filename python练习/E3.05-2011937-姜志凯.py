m,n=eval(input().replace(' ',','))
if m%2==0 and n%2!=0:
    print((m/2)*n)
elif n%2==0:
    print((n/2)*m)
else:
    print((m//2)*n+(n//2))
