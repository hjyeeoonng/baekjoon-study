import sys

N,M=map(int,sys.stdin.readline().split())

m=[]
visit=[]
for i in range(N):
    m.append(list(sys.stdin.readline().strip()))
visit=[[0]*M for i in range(N)]
print(visit)
