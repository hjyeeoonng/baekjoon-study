import sys
from collections import deque
N,M,R=map(int,sys.stdin.readline().split())
node=[0]*N
dic={}
def dfs(num,s):
    if node[num-1]==0:
        node[num-1]=s
        if num in dic:
            temp=dic[num]
            temp.sort()
            for i in temp:
               que.appendleft(i)
        return True
    else:
        return False
        
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    if a not in dic:
        dic[a]=[b]
    else:
        dic[a]+=[b]
    if b not in dic:
        dic[b]=[a]
    else:
        dic[b]+=[a]

que=deque()
que.append(R)

s=1
while que:
    t=dfs(que.popleft(),s)
    if t==True:
        s+=1

for i in node:
    print(i)
