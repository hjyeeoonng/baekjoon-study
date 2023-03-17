import sys
N=int(sys.stdin.readline())
numlist=[0 for i in range(10000)]
for i in range(N):
    num=int(sys.stdin.readline())
    numlist[num-1]+=1
for i in range(len(numlist)):
    if numlist[i] != 0:
        for j in range(numlist[i]):
            print(i+1)
