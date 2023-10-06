import sys
from collections import deque
n=[0]*100001
N,K=map(int,sys.stdin.readline().split())
def bfs(num):
    if num[0]-1>=0 and num[0]-1<=100000:
        if n[num[0]-1]==0:
            que.append((num[0]-1,num[1]+1))
            n[num[0]-1]=1
    if num[0]+1>=0 and num[0]+1<=100000:
        if n[num[0]+1]==0:
            que.append((num[0]+1,num[1]+1))
            n[num[0]+1]=1
    if num[0]*2>=0 and num[0]*2<=100000:
        if n[num[0]*2]==0:
            que.append((num[0]*2,num[1]+1))
            n[num[0]*2]=1
que=deque()
que.append((N,0))
while que:
    temp=que.popleft()
    if temp[0]== K:
        print(temp[1])
        break
    bfs(temp)
