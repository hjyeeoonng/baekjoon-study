import sys
N=int(sys.stdin.readline())
km=list(map(int,sys.stdin.readline().split()))
charge=list(map(int,sys.stdin.readline().split()))

res=0
mincharge=charge[0]
for i in range(len(km)):
    res+=km[i]*mincharge
    if charge[i+1]<mincharge:
        mincharge=charge[i+1]
print(res)
