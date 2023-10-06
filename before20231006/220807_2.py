#ATM
N=int(input())
t=list(map(int,input().split()))
t.sort()
time=0
for i in range(N):
    time+=t[i]*(N-i)
print(time)
