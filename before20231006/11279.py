import sys
import heapq
T=int(sys.stdin.readline())
a=[]
for i in range(T):
    cmd=sys.stdin.readline().strip()
    if cmd=='0':
        if len(a)>0:
            print(-heapq.heappop(a))
        else:
            print(0)
    else:
        heapq.heappush(a,-int(cmd))
