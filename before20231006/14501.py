import sys
N=int(sys.stdin.readline())
s=[]
for i in range(N):
    s.append(list(map(int,sys.stdin.readline().split())))
profit=[]
def choice(ret,day,N):
    if day<N:
        if day+s[day][0]<=N:
            choice(ret,day+1,N)
            choice(ret+s[day][1],day+s[day][0],N)
        else:
            profit.append(ret)
    else:
        profit.append(ret)
choice(0,0,N)
print(max(profit))
