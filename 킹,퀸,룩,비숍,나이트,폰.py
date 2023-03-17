import sys
a=list(map(int,sys.stdin.readline().split()))
b=[1,1,2,2,2,8]
for i in range(len(a)):
    print(b[i]-a[i],end=' ')
