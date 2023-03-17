jb=list(map(int,input().split()))
jewel=[]
bag=[]
for i in range(jb[0]):
    jewel.append(list(map(int,input().split())))
for i in range(jb[1]):
    bag.append(int(input()))
jewel.sort(key=lambda x:x[1])
jewel.reverse()
bag.sort()
R=0
for i in bag:
    for j in range(len(jewel)):
        if jewel[j][0]<i and jewel[j][0]!=-1:
            R+=jewel[j][1]
            jewel[j][0]=-1
            break
print(R)
