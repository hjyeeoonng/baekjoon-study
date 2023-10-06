import sys
import math
N=int(sys.stdin.readline())
for i in range(N):
    x1,x2,y1,y2,r1,r2=map(int,sys.stdin.readline().split())
    dis=math.sqrt(pow((x1-y1),2)+pow((y2-x2),2))
    if dis==0.0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        temp=float(r1+r2)
        print(temp,dis)
        if temp>dis:
            print(2)
        elif temp==dis:
            print(1)
        else:
            print(0)
