import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
miro=[]
for i in range(N):
    miro.append(list(map(int,sys.stdin.readline().strip())))
def bfs(miro):
    visited=[]
    for i in range(len(miro)):
        visited.append([0 for j in range(len(miro[0]))])
    q=deque()
    q.append([0,0,0])
    count=[]
    while q:
        n=q.popleft()
        if n[0]==N-1 and n[1]==M-1:
            return n[2]
        if miro[n[0]][n[1]]==1 and visited[n[0]][n[1]]==0:
            visited[n[0]][n[1]]=1
            if n[0]-1>=0:
                if visited[n[0]-1][n[1]]==0:
                    q.append([n[0]-1,n[1],n[2]+1])
            if n[0]+1<=len(visited)-1:
                if visited[n[0]+1][n[1]]==0:
                    q.append([n[0]+1,n[1],n[2]+1])
            if n[1]-1>=0:
                if visited[n[0]][n[1]-1]==0:
                    q.append([n[0],n[1]-1,n[2]+1])
            if n[1]+1<=len(visited[0])-1:
                if visited[n[0]][n[1]+1]==0:
                    q.append([n[0],n[1]+1,n[2]+1])
print(bfs(miro)+1)
