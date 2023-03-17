import sys
N=int(sys.stdin.readline())
spot=[]
for i in range(N):
    temp=list(map(float,sys.stdin.readline().split()))
    temp[1]=temp[1]+temp[0]/1000000
    spot.append(temp)
spot.sort(key=lambda x : x[1])
for i in spot:
    print(int(i[0]),round(i[1]))
