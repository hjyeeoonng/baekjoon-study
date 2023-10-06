import sys
from collections import deque
n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
nlist=[0 for i in range(1000001)]
ans = [-1 for i in range(n)]
for i in nums:
    nlist[i]+=1

stack = deque()

stack.append(nums[0])
for i in range(1,n):
    c=1
    while stack:
        if nlist[nums[i]]>nlist[stack[-1]]:
            while ans[i-c]!=-1:
                c+=1
            ans[i-c]=nums[i]
            stack.pop()
        else:
            break
        c+=1
    stack.append(nums[i])

for i in ans:
    print(i,end=" ")