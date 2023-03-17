import sys
from collections import Counter

N,M,B=map(int,sys.stdin.readline().split())
block=[]
for i in range(N):
    temp=map(int,sys.stdin.readline().split())
    for i in temp:
        block.append(i)

block.sort(reverse=True)

minTime=N*M*257
floor=-1
for i in range(0,257):
    plusblock=0
    minusblock=0
    for j in block:
        if j>i:
            minusblock+=(j-i)
        elif j==i:
            continue
        else:
            plusblock+=(i-j)
    if minusblock+B<plusblock:
        continue
    else:
        Time=plusblock*1+minusblock*2
        if Time<=minTime:
            minTime=Time
            floor = i
print(minTime,floor)
