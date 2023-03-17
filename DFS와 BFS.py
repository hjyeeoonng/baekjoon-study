from collections import deque
N,M,V=map(int,input().split())
graph_list={}

def make_graph(temp):
    if temp[0] in graph_list:
        t=graph_list[temp[0]]
        t.append(temp[1])
        t.sort()
        graph_list[temp[0]]=t
    else:
        graph_list.setdefault(temp[0])
        tt=[temp[1]]
        tt.sort()
        graph_list[temp[0]]=tt
        
for i in range(M):
    temp=list(map(int,input().split()))
    temp_=[temp[1],temp[0]]
    make_graph(temp)
    make_graph(temp_)

def BFS(graph_list,root):
    queue=deque([root])
    visited=[]
    while queue:
        n=queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph_list:
                for j in graph_list[n]:
                    if j not in visited:
                        queue.append(j)
    return visited

def DFS(graph_list,root):
    stack=[root]
    visited=[]
    while stack:
        n=stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph_list:
                t=graph_list[n]
                t.reverse()
                for j in t:
                    if j not in visited:
                        stack.append(j)
    return visited

bfs=BFS(graph_list,V)
dfs=DFS(graph_list,V)
for i in dfs:
    print(i,end=' ')
print('')
for i in bfs:
    print(i,end=' ')
