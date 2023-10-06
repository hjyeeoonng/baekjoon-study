import heapq
import sys
T=int(sys.stdin.readline())
for i in range(T):
    N=int(sys.stdin.readline())
    minque=[]
    maxque=[]
    for j in range(N):
        cmd=list(sys.stdin.readline().split())
        cmd[1]=int(cmd[1])
        if cmd[0]=='I':
            heapq.heappush(minque,cmd[1])
            heapq.heappush(maxque,-cmd[1])
        else:
            if len(minque)>0:
                if cmd[1]==-1:
                    temp=heapq.heappop(minque)
                    maxque.remove(-temp)
                else:
                    temp=heapq.heappop(maxque)
                    minque.remove(-temp)
            
    if len(minque)==0:
        print('EMPTY')
    elif len(minque)==1:
        print(minque[0],minque[0])
    else:
        resmax=heapq.heappop(maxque)
        resmin=heapq.heappop(minque)
        print(-resmax,resmin)

