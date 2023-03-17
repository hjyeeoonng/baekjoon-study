import sys
import math
num=int(sys.stdin.readline())
n=[0]*(num+1)
nlist=[]
for i in range(1,int(math.sqrt(num))+1):
    nlist.append(i*i)
temp=num-4
N=0
while temp!=0:
    temp-=pow(int(math.sqrt(temp)),2)
    print(temp)
    N+=1
print(N-1)
