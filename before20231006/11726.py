import sys
n=int(sys.stdin.readline())
N=[0]*(n+1)
if n>=1:
    N[1]=1
if n>=2:
    N[2]=3
for i in range(3,n+1):
    N[i]=N[i-2]*2+N[i-1]
print(N[-1]%10007)
