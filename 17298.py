import sys
from collections import deque
n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

stack=deque()
ans=[-1 for i in range(n)]

stack.append(nums[0])

for i in range(1,n):
    c=1
    while stack:
        if nums[i] > stack[-1]:
            while ans[i-c]!=-1:
                c+=1
            ans[i-c]=nums[i]
            stack.pop()
            c+=1
        else:
            break
    stack.append(nums[i])

for i in ans:
    print(i,end=" ")