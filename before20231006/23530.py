import sys
N = int(sys.stdin.readline())
for i in range(N):
    a,b = sys.stdin.readline().split()
    if int(a) > 1:
        print(int(a)-1)
    else:
        print(int(a)+int(b)-1)
