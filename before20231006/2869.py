import sys
import math
A,B,V=map(int,sys.stdin.readline().split())
V-=A
print(math.ceil(V/(A-B)+1))
