n=eval(input())
j=0
for i in eval(input().replace(' ',',')):
    if i==1:
        print('HARD')
        j=1
        break
if j==0:
    print('EASY')
