import sys
N=sys.stdin.readline()
nlist=[]
nnlist=[]
for i in range(int(N)):
    temp=sys.stdin.readline()[:-1]
    nlist.append(temp)
nlist=list(set(nlist))
nlist.sort(key=lambda x:len(x))
for i in nlist:
    print(i)
