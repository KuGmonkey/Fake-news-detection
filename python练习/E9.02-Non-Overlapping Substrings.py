s=input()
if 'AB' not in s or 'BA' not in s:
    print('NO')
else:
    if s.replace('AB','$',1).count('BA')>0 or s.replace('BA','$',1).count('AB')>0:
        print('YES')
    else:
        print('NO')
