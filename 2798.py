import sys
N,M=map(int,sys.stdin.readline().split())
card=list(map(int,sys.stdin.readline().split()))
ans=0
for i in range(len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            result = card[i]+card[j]+card[k]
            if result<=M and result>ans:
                ans=result
print(ans)
