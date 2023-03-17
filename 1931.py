import sys
N=int(sys.stdin.readline())
meet=[]
for i in range(N):
    start,end=map(int,sys.stdin.readline().split())
    meet.append([start,end,end+start/(start+1)])
meet.sort(key= lambda x:x[2])
cnt=0
end=0
for i in meet:
    if i[0]==i[1] and i[0]>=end:
        cnt+=1
        end=i[1]
    elif i[1]>end and i[0]>=end:
        end=i[1]
        cnt+=1
print(cnt)
