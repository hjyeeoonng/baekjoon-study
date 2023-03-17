import sys
nlist=list(map(int,sys.stdin.readline().split()))
nl=[]
nl.append(nlist[3]-nlist[1])
nl.append(nlist[2]-nlist[0])
nl.append(nlist[1]-0)
nl.append(nlist[0]-0)
print(min(nl))
