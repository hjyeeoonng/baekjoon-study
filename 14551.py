import sys
N,M = map(int,sys.stdin.readline().split())
R=1
for i in range(N):
    num = int(sys.stdin.readline())
    if num !=0:
        R*=num
print(R%M)

