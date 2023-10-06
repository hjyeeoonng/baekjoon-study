import sys
total=int(sys.stdin.readline())
N=int(sys.stdin.readline())
c=0
for i in range(N):
    temp=list(map(int,sys.stdin.readline().split()))
    c+=temp[0]*temp[1]
if c==total:
    print('Yes')
else:
    print('No')
