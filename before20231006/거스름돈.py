s=int(input())
s=1000-s
R=0
for i in [500,100,50,10,5,1]:
    R+=s//i
    s%=i
print(R)
