import sys
from collections import deque
dic=[0]*101
N,M=map(int,sys.stdin.readline().split())
dic2={}
for i in range(N+M):
    a,b=map(int,sys.stdin.readline().split())
    if a in dic2:
        dic2[a]+=[b]
    else:
        dic2[a]=[b]
que=deque()
que.append((1,0))
def bfs(num,n):
    if num in dic2:
        temp=dic2[num]
        for j in temp:
            for i in range(1,7):
                if j+i<=100:
                    if dic[j+i]==0:
                        que.append((j+i,n+1))
                        dic[j+i]=1
    else:
        for i in range(1,7):
            if num+i<=100:
                if dic[num+i]==0:
                    que.append((num+i,n+1))
                    dic[num+i]=1
while que:
    t=que.popleft()
    if t[0]==100:
        break
    bfs(t[0],t[1])
print(t[1])
