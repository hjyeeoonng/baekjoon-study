import sys
from collections import deque
que=deque()
N=int(sys.stdin.readline())
for i in range(N):
    cmd=sys.stdin.readline().strip()
    if cmd[:3]=='pus':
        cmd,num=cmd.split()
        num=int(num)
    if cmd=='push':
        que.append(num)
    elif cmd=='pop':
        if len(que)>0:
            temp=que.popleft()
            print(temp)
        else:
            print(-1)
    elif cmd=='size':
        print(len(que))
    elif cmd=='empty':
        if len(que)==0:
            print(1)
        else:
            print(0)
    elif cmd=='front':
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
    else:
        if len(que)==0:
            print(-1)
        else:
            print(que[-1])
