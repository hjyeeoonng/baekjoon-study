import sys
p=0
m=0
for i in range(10):
    a,b=map(int,sys.stdin.readline().split())
    p+=(b-a)
    if p>m:
        m=p
print(m)
