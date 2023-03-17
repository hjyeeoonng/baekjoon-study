N=int(input())
nlist=[]
for i in range(N):
    nlist.append(list(map(int,input().split())))
nlist.sort(key=lambda x:x[0])
print(nlist)
