s=input()
l=['A','E','I','O','U']
t1=0
t2=0
for i in range(len(s)-2):
    if s[i] in l:
        if s[i+1] in l and s[i+2] in l:
            t1=1;
        else:
            pass
    else:
        pass
x1=set(s)
x=list(x1)
for j in range(5):
    if l[j] in x:
        x.remove(l[j])
if len(x)>=5:
    t2=1
if t1==1 and t2==1:
    print('GOOD')
else:
    print('BAD')
