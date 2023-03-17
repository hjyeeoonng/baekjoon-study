import sys
w=[[0]*100 for i in range(100)]
N=int(sys.stdin.readline())
for i in range(N):
    a,b=map(int,sys.stdin.readline().split())
    for j in range(a-1,a+9):
        for k in range(b-1,b+9):
            w[j][k]=1
res=0
for i in w:
    res+=sum(i)
print(res)
