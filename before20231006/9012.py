import sys
l=[]
N = int(sys.stdin.readline())
for i in range(N):
    l.append(sys.stdin.readline().rstrip())
for i in l:
    left=0
    right=0
    for j in i:
        if j == '(':
            left+=1
        elif j == ')' and left>0:
            left-=1
        else:
            right+=1
    if left+right==0:
        print('YES')
    else:
        print('NO')

