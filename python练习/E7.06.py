n=""
for i in range(int(input())):
    n+=input()
print(n.count("00")+n.count("11")+1)
