import sys
A=[]
B=[]
for i in range(3):
    a,b=map(int,sys.stdin.readline().split())
    if a in A:
        A.remove(a)
    else:
        A.append(a)
    if b in B:
        B.remove(b)
    else:
        B.append(b)
print(A[0],B[0])
