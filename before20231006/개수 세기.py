#과제 안 내신 분
plist=[]
for i in range(30):
    plist.append(i+1)
for i in range(28):
    p=int(input())
    plist.remove(p)
plist.sort()
print(plist[0])
print(plist[1])
