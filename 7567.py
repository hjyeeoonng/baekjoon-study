import sys
text=sys.stdin.readline().strip()
ans=10
temp=text[0]
for i in range(1,len(text)):
    if temp!=text[i]:
        ans+=10
    else:
        ans+=5
    temp=text[i]
print(ans)
