import sys
from collections import deque

que=deque()


Testcase=int(sys.stdin.readline())

for i in range(Testcase):
    
    N,M=map(int,sys.stdin.readline().split())
    paper=list(map(int,sys.stdin.readline().split()))
    
    for i in paper:
        que.append(i)
    
    paperprint=0
    
    while 1:
        a = que.popleft()
        if len(que)>0:
            if a>=max(que):
                paperprint+=1
                M-=1
                if M==-1:
                    break
            else:
                que.append(a)
                M-=1
                if M==-1:
                    M=len(que)-1
        else:
            paperprint+=1
            break

    print(paperprint)

    que=deque()
