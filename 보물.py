a=input()
b=list(map(int,input().split()))
c=list(map(int,input().split()))
b.sort()
c.sort(reverse=True)
R=0
for i in range(len(b)):
    R+=b[i]*c[i]
print(R)

