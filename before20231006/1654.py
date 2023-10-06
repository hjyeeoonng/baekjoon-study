import sys
K, N = map(int,sys.stdin.readline().split())
line=[]
TotalLineLength=0
R=0

def calline(cm):
    calresult = 0
    for i in line:
        calresult+=i//cm
    return calresult

for i in range(K):
    newline = int(sys.stdin.readline())
    line.append(newline)
for i in line : TotalLineLength += i

start=1
end=TotalLineLength//N
mid = (start+end)//2

if calline(end)==N:
    print(end)
else: 
    while start+1 < end:
        c=calline(mid)
        #print(start,end,mid,c)
        if c > N:
            start=mid
            mid = (start+end)//2
        elif c < N:
            end=mid
            mid = (start+end)//2
        else:
            if R<mid:
                R=mid
            start=mid
            mid = (start+end)//2
    print(mid)
