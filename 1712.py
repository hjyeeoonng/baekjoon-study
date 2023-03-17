a,b,c=map(int,input().split())
i=0
while a+b*i>c*i:
    i+=1

print(i+1)
