import sys
N=int(sys.stdin.readline())
i=0
N-=1
while 1:
    N-=(i*6)
    if N<=0:
        print(i+1)
        break
    i+=1
