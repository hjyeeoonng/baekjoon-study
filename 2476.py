import sys
N=int(sys.stdin.readline())
res=[]
for i in range(N):
    a,b,c=map(int,sys.stdin.readline().split())
    if a==b and b==c:
        res.append(10000+a*1000)
    elif a==b:
        res.append(1000+a*100)
    elif b==c:
        res.append(1000+b*100)
    elif a==c:
        res.append(1000+a*100)
    else:
        res.append(max([a,b,c])*100)
print(max(res))
