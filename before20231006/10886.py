import sys
N=int(sys.stdin.readline())
zero=0
nzero=0
for i in range(N):
    survey=int(sys.stdin.readline())
    if survey==0:
        zero+=1
    else:
        nzero+=1
if zero>nzero:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
