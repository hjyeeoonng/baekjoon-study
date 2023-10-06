import sys
sys.setrecursionlimit(10**6)

N,M=map(int,sys.stdin.readline().split())
visit=[[0 for j in range(M)] for i in range(N)]
m=[]

for i in range(N):
    m.append(list(map(int,sys.stdin.readline().strip())))

def dfs(pos,result):
    
    visit[pos[0]][pos[1]]=1#방문처리
    
    if pos[0]==N-1 and pos[1]==M-1:
        if result>pos[3]:
            result=pos[3]
        visit[pos[0]][pos[1]]=0
    
    if pos[2]==0:
        if pos[0]+1<N:
            if visit[pos[0]+1][pos[1]]==0 and m[pos[0]+1][pos[1]]==0:
                a=dfs([pos[0]+1,pos[1],0,pos[3]+1],result)
                if a<result:
                    result=a
        if pos[0]-1>=0:
            if visit[pos[0]-1][pos[1]]==0 and m[pos[0]-1][pos[1]]==0:
                a=dfs([pos[0]-1,pos[1],0,pos[3]+1],result)
                if a<result:
                    result=a
        if pos[1]+1<M:
            if visit[pos[0]][pos[1]+1]==0 and m[pos[0]][pos[1]+1]==0:
                a=dfs([pos[0],pos[1]+1,0,pos[3]+1],result)
                if a<result:
                    result=a
        if pos[1]-1>=0:
            if visit[pos[0]][pos[1]-1]==0 and m[pos[0]][pos[1]-1]==0:
                a=dfs([pos[0],pos[1]-1,0,pos[3]+1],result)
                if a<result:
                    result=a
    else:
        if pos[0]+1<N:
            if visit[pos[0]+1][pos[1]]==0:
                if m[pos[0]+1][pos[1]]==0:#벽아니어서 부술필요없음
                    a=dfs([pos[0]+1,pos[1],1,pos[3]+1],result)
                    if a<result:
                        result=a
                else:#벽일경우 부수기
                    a=dfs([pos[0]+1,pos[1],0,pos[3]+1],result)
                    if a<result:
                        result=a
        if pos[0]-1>=0:
            if visit[pos[0]-1][pos[1]]==0:
                if m[pos[0]-1][pos[1]]==0:
                    a=dfs([pos[0]-1,pos[1],1,pos[3]+1],result)
                    if a<result:
                        result=a
                else:#벽일경우 부수기
                    a=dfs([pos[0]-1,pos[1],0,pos[3]+1],result)
                    if a<result:
                        result=a
        if pos[1]+1<M:
            if visit[pos[0]][pos[1]+1]==0:
                if m[pos[0]][pos[1]+1]==0:
                    a=dfs([pos[0],pos[1]+1,1,pos[3]+1],result)
                    if a<result:
                        result=a
                else:
                    a=dfs([pos[0],pos[1]+1,0,pos[3]+1],result)
                    if a<result:
                        result=a
        if pos[1]-1>=0:
            if visit[pos[0]][pos[1]-1]==0:
                if m[pos[0]][pos[1]-1]==0:
                    a=dfs([pos[0],pos[1]-1,1,pos[3]+1],result)
                    if a<result:
                        result=a
                else:
                    a=dfs([pos[0],pos[1]-1,0,pos[3]+1],result)
                    if a<result:
                        result=a

    visit[pos[0]][pos[1]]=0
    return result

print(dfs([0,0,1,0],N*M)+1)