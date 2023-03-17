a=list(map(int,input().split()))
b=list(map(int,input().split()))
b.sort(reverse=True)
print(b[a[1]-1])
