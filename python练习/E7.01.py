a=[0,0,0,0,0]
for i in range(5):
    a[i]=list(map(int,input().split()))
for x in range(5):
    for y in range(5):
        if a[x][y]!=0:
            print(abs(x-2)+abs(y-2))
            break

