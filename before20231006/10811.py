import sys
N,M=map(int,sys.stdin.readline().split())
nlist=[]
for i in range(N):
    nlist.append(i+1)
    
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    temp=nlist[a-1:b]
    temp=temp[::-1]
    cnt=0
    for j in temp:
        nlist[a-1+cnt]=j
        cnt+=1
for i in nlist:
    print(i,end=' ')
