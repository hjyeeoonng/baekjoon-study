import sys
from collections import deque
n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

stack=deque()
ans=""

for i in nums:
    for j in range(len(stack)):
        if stack[-1]<i:
            ans+=" "+str(i)
            stack.pop()
    if len(stack)==0:
        ans+=" -1"
    stack.append(i)
ans+=" -1"
print(ans.strip())