from collections import deque
import sys

testcase = int(sys.stdin.readline())

def bfs(now, des):
    if now==des:
        return 0
    else:
        que=deque()
        que.append([now[0],now[1],0])
    while(que):
        pos = que.popleft()
        while(visit[pos[0]][pos[1]]):
            pos = que.popleft()
        visit[pos[0]][pos[1]]=1#방문처리
        
        if [pos[0],pos[1]]==des:
            return pos[2]#몇번째인지 리턴
        else:
            if pos[0]+1<n and pos[1]+2<n:
                if visit[pos[0]+1][pos[1]+2]==0:
                    que.append([pos[0]+1,pos[1]+2,pos[2]+1])#방문 안했으면 추가
            if pos[0]+1<n and pos[1]-2>=0:
                if visit[pos[0]+1][pos[1]-2]==0:
                    que.append([pos[0]+1,pos[1]-2,pos[2]+1])#방문 안했으면 추가
            if pos[0]+2<n and pos[1]-1>=0:
                if visit[pos[0]+2][pos[1]-1]==0:
                    que.append([pos[0]+2,pos[1]-1,pos[2]+1])#방문 안했으면 추가
            if pos[0]+2<n and pos[1]+1<n:
                if visit[pos[0]+2][pos[1]+1]==0:
                    que.append([pos[0]+2,pos[1]+1,pos[2]+1])#방문 안했으면 추가
            if pos[0]-1>=0 and pos[1]+2<n:
                if visit[pos[0]-1][pos[1]+2]==0:
                    que.append([pos[0]-1,pos[1]+2,pos[2]+1])#방문 안했으면 추가
            if pos[0]-1>=0 and pos[1]-2>=0:
                if visit[pos[0]-1][pos[1]-2]==0:
                    que.append([pos[0]-1,pos[1]-2,pos[2]+1])#방문 안했으면 추가
            if pos[0]-2>=0 and pos[1]+1<n:
                if visit[pos[0]-2][pos[1]+1]==0:
                    que.append([pos[0]-2,pos[1]+1,pos[2]+1])#방문 안했으면 추가
            if pos[0]-2>=0 and pos[1]-1>=0:
                if visit[pos[0]-2][pos[1]-1]==0:
                    que.append([pos[0]-2,pos[1]-1,pos[2]+1])#방문 안했으면 추가

for i in range(testcase):
    n=int(sys.stdin.readline())
    now=list(map(int,sys.stdin.readline().split()))
    des=list(map(int,sys.stdin.readline().split()))
    visit = [[0 for i in range(n)] for j in range(n)]                
    print(bfs(now, des))
