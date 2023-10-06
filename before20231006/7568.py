import sys
N=int(sys.stdin.readline())
d=[]
for i in range(N):
    d.append(list(map(int,sys.stdin.readline().split())))
for i in d:
    count=0
    for j in d:
        if i[0]<j[0] and i[1]<j[1]:
            count+=1
    print(count+1,end=' ')
