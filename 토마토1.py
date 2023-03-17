from collections import deque
import sys
M,N=map(int,sys.stdin.readline().split())
box=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
day=[]

def bfs(p,d):
    que=deque()#큐선언
    #방문했음으로 바꾸기
    if box[p[0]][p[1]]==0:
        box[p[0]][p[1]]=2
    #상하좌우방향 안익은 거 큐에 넣기
    if p[1]+1>=0 and p[1]+1<M:
        if box[p[0]][p[1]+1]==0:
            que.append([[p[0],p[1]+1],d+1])
    if p[1]-1>=0 and p[1]-1<M:
        if box[p[0]][p[1]-1]==0:
            que.append([[p[0],p[1]-1],d+1])
    if p[0]+1>=0 and p[0]+1<N:
        if box[p[0]+1][p[1]]==0:
            que.append([[p[0]+1,p[1]],d+1])
    if p[0]-1>=0 and p[0]-1<N:
        if box[p[0]-1][p[1]]==0:
            que.append([[p[0]-1,p[1]],d+1])
    #큐 처리하기
    while que:
        print(que)
        n=que.popleft()
        print('나온거',n, que)
        bfs(n[0],n[1])
def bfs1(p,d):
    que=deque()
    que.append([p,d])
    
    

for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            bfs([i,j],1)

print(box)
