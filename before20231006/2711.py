import sys
N=int(sys.stdin.readline())
for i in range(N):
    a,b=sys.stdin.readline().split()
    a=int(a)
    print(b[:a-1]+b[a:])
