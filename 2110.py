import sys
N,C=map(int,sys.stdin.readline().split())
house=[]
for i in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()
checked=[0]*len(house)
checked[0]=1
checked[-1]=1
C-=2
R=house[-1]-house[0]
if C>0:
    lo=house[0]
    hi=house[-1]
    mid=lo+hi//2
    while C=0:
        
        mid=lo+hi//2
print(R)
