a=list(map(int,input().split()))
b=list(map(int,input().split()))
b.sort()
R=1
tape=a[1]
for i in range(len(b[1:])):
    if b[i+1]-b[i]>=tape:
        R+=1
        tape=a[1]
    else:
        tape-=b[i+1]-b[i]
print(R)

