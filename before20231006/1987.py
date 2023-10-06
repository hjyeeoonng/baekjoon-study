a,b=map(int,input().split())
alpa=[]
for i in range(a):
    alpa.append(input())

visit=[[0 for i in range(b)] for j in range(a)]
string=""

def dfs(x,y,alpa,string):
    string=string+alpa[y][x]
    visit[y][x]=1
    result=[]
    if y-1>=0:
        if visit[y-1][x]==0:
            if alpa[y-1][x] not in string:
                result.append(dfs(x,y-1,alpa,string))
    if y+1<a:
        if visit[y+1][x]==0:
            if alpa[y+1][x] not in string:
                result.append(dfs(x,y+1,alpa,string))
    if x-1>=0:
        if visit[y][x-1]==0:
            if alpa[y][x-1] not in string:
                result.append(dfs(x-1,y,alpa,string))
    if x+1<b:
        if visit[y][x+1]==0:
            if alpa[y][x+1] not in string:
                result.append(dfs(x+1,y,alpa,string))
    visit[y][x]=0
    if result!=[]:
        return max(result)
    else:
        return len(string)

print(dfs(0,0,alpa,string))
