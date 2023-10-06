#k 층 n 호
import sys
T=int(sys.stdin.readline())
for i in range(T):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    apart=[[0] * n for temp in range(k+1)]
    for j in range(n):
        apart[0][j]=(j+1)
    for j in range(n):
        for m in range(k):
            if j==0:
                apart[m+1][j]=apart[m][j]
            else:
                apart[m+1][j]=(apart[m][j]+apart[m+1][j-1])
    print(apart[k][n-1])
