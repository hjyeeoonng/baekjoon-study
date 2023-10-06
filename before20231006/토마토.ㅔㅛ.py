import sys
from collections import deque
M,N=map(int,sys.stdin.readline().split())
box=[]
for i in range(N):
    box.append(list(map(int,sys.stdin.readline().split())))
print(box)
