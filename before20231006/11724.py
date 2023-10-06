import sys
sys.setrecursionlimit(2500)
node,edge=map(int,sys.stdin.readline().split())
diction={}
for i in range(edge):
    a,b=map(int,sys.stdin.readline().split())
    if a in diction:
        diction[a]+=[b]
    else:
        diction[a]=[b]
    if b in diction:
        diction[b]+=[a]
    else:
        diction[b]=[a]

nodes=[0]*node
def bfs(n):
    if nodes[n-1]!=1:
        nodes[n-1]=1
        if n in diction:
            for j in diction[n]:
                bfs(j)
total=0
for i in range(node):
    if nodes[i]==0:
        total+=1
        bfs(i+1)
print(total)
