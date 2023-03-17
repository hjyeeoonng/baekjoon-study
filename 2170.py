import sys
N=int(sys.stdin.readline())
line=[]
for i in range(N):
    line.append(list(map(int,sys.stdin.readline().split())))
line.sort(key=lambda x : x[0])
lo=line[0][0]
hi=line[0][1]
R=0
for i in line[1:]:
    if i[0]<=hi:
        if hi<i[1]:
            hi=i[1]
    else:
        R+=hi-lo
        lo=i[0]
        hi=i[1]
R+=hi-lo
print(R)
