alist=list(map(int,input().split()))
blist=[]
for i in range(alist[0]):
    blist.append(int(input()))
K=alist[1]
blist.reverse()
R=0
for i in blist:
    R+=K//i
    K%=i
print(R)
