import sys
import heapq
N=int(sys.stdin.readline())
sea=[]
for i in range(N):
    sea.append(list(map(int,sys.stdin.readline().split())))
print(sea)
visit=[[0]*N for i in range(N)]
print(visit)

sharksize=2
que=[]
for i in range(len(sea)):
    for j in range(len(sea[i])):
        if sea[i][j]==9:
            pos=(i,j)
            heapq.heappush(que,pos)

while que:
    temp=heapq.heappop(que)
    visit[temp[0]][temp[1]]=1
    if temp[1]+1<N:
        if visit[temp[0]][temp[1]+1]!=1:
            heapq.heappush(que,(temp[0],temp[1]+1))
    if temp[0]-1>=0:
        if visit[temp[0]-1][temp[1]]!=1:
            heapq.heappush(que,(temp[0]-1,temp[1]))
    if temp[0]+1<N:
        if visit[temp[0]+1][temp[1]]!=1:
            heapq.heappush(que,(temp[0]+1,temp[1]))
    if temp[1]-1>=0:
        if visit[temp[0]][temp[1]-1]!=1:
            heapq.heappush(que,(temp[0],temp[1]-1))
    
