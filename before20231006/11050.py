import sys
N,K=map(int,sys.stdin.readline().split())
if K==0:
    print(1)
elif K==N:
    print(1)
else:
    result=N
    for i in range(K-1):
        result*=(N-(i+1))
    while K>=1:
        result/=K
        K-=1
    print(int(result))

