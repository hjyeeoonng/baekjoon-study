import sys
N=int(sys.stdin.readline())
def GCD(a,b):
    n=a%b
    if n==0:
        return b
    else:
        return GCD(b,n)
for i in range(N):
    A,B=map(int,sys.stdin.readline().split())
    if A>B:
        temp=GCD(A,B)
        print(int(A*B/temp))
    else:
        temp=GCD(B,A)
        print(int(A*B/temp))
    
    
