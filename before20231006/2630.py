import sys
N=int(sys.stdin.readline())
totalblue=0
totalwhite=0

pp=[]

for i in range(N):
    pp.append(list(map(int,sys.stdin.readline().split())))

def check(n1,n2):
    ret=pp[n1][n2]+pp[n1][n2+1]+pp[n1+1][n2]+pp[n1+1][n2+1]
    if ret>=5:
        a=[ret%5,4-ret%5-ret//5,ret//5]
    else:
        a=[ret,4-ret,0]
    return a

while N>=2:
    nlists=[]
    for i in range(0,len(pp),2):
        nlist=[]
        for j in range(0,len(pp),2):
            res=check(i,j)
            if res[0]==4:
                nlist.append(1)
            elif res[1]==4:
                nlist.append(0)
            else:
                totalblue+=res[0]
                totalwhite+=res[1]
                nlist.append(5)
        nlists.append(nlist)
    pp=nlists
    N/=2
if pp[0][0]==1:
    totalblue+=1
elif pp[0][0]==0:
    totalwhite+=1
print(totalwhite)
print(totalblue)
