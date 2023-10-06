import sys
from collections import deque
N=int(sys.stdin.readline().strip())
map_=[]
for i in range(N):
    map_.append(list(map(int,sys.stdin.readline().strip())))

def dfs(x,y):
    q=deque()
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return 0
    if map_[x][y]==1:
        map_[x][y]=0
        re=0
        re+=dfs(x,y+1)
        re+=dfs(x+1,y)
        re+=dfs(x,y-1)
        re+=dfs(x-1,y)
        return 1+re
    return 0

result=[]
for i in range(N):
    for j in range(N):
        n=dfs(i,j)
        if n!=0:
            result.append(n)

result.sort()
print(len(result))
for i in result:
    print(i)
