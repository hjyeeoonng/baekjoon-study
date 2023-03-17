from collections import deque
import sys
T=int(sys.stdin.readline())
sys.setrecursionlimit(10**4)

def dfs(p):
    q=deque()
    if p[1]+1>=0 and p[1]+1<M:
        if land[p[0]][p[1]+1]==1:
            land[p[0]][p[1]+1]=0
            q.append([p[0],p[1]+1])
    if p[1]-1>=0 and p[1]-1<M:
        if land[p[0]][p[1]-1]==1:
            land[p[0]][p[1]-1]=0
            q.append([p[0],p[1]-1])
    if p[0]+1>=0 and p[0]+1<N:
        if land[p[0]+1][p[1]]==1:
            land[p[0]+1][p[1]]=0
            q.append([p[0]+1,p[1]])
    if p[0]-1>=0 and p[0]-1<N:
        if land[p[0]-1][p[1]]==1:
            land[p[0]-1][p[1]]=0
            q.append([p[0]-1,p[1]])
    while q:
        n=q.popleft()
        dfs(n)
    
for i in range(T):
    N,M,K=map(int,sys.stdin.readline().split())
    land=[[0 for i in range(M)] for i in range(N)]
    for j in range(K):
        p1,p2=map(int,sys.stdin.readline().split())
        land[p1][p2]=1
    total=0
    for i in range(N):
        for j in range(M):
            if land[i][j]==1:
                dfs([i,j])
                total+=1
    print(total)
