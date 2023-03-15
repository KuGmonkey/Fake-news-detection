d={}
for i in range(eval(input())):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
r={y:x for x,y in d.items()}
print(r[max(r)])
