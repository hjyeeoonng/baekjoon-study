import sys
n=list(map(int,sys.stdin.readline().split()))
alist=[]
blist=[]
for i in range(n[0]):
    alist.append(list(map(int,sys.stdin.readline().split())))
for i in range(n[0]):
    blist.append(list(map(int,sys.stdin.readline().split())))
for i in range(n[0]):
    for j in range(n[1]):
        print(alist[i][j]+blist[i][j], end=" ")
    print()
