import sys
import heapq
T=int(sys.stdin.readline())
a=[]
for i in range(T):
    cmd=sys.stdin.readline().strip()
    cmd=int(cmd)
    if cmd==0:
        if len(a)>0:
            print(heapq.heappop(a)[1])
        else:
            print(0)
    else:
        add=0
        if cmd<0:
            add=-0.1
        temp=(abs(cmd)+add,cmd)
        heapq.heappush(a,temp)
