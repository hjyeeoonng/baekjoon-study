s=input().split('-')
for i in range(len(s)):
    s[i]=sum(list(map(int,s[i].split('+'))))
R=0
for i in range(len(s)):
    if i==0:
        R+=s[i]
    else:
        R-=s[i]
print(R)
