import sys
N=int(sys.stdin.readline())
stack=[]
for i in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        if len(stack)>0:
            stack.pop()
print(sum(stack))
