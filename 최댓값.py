import sys
nlist=[]
for i in range(9):
    nlist.append(list(map(int,sys.stdin.readline().split())))
maxvalue=-1
ri=0
rj=0
for i in range(9):
    for j in range(9):
        if nlist[i][j]>maxvalue:
            maxvalue=nlist[i][j]
            ri=i+1
            rj=j+1
print(maxvalue)
print(ri,rj)
