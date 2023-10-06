import sys
n=int(sys.stdin.readline())
stack=[]
c=1#c=넣어야 할 수
result=[]
flag=0
for i in range(n):
    num=int(sys.stdin.readline()) #새로 들어온 수
    #새로 들어온 수가 넣어야 할 수 보다 같거나 크면 출력 가능
    #작은 경우,TOP이 num 과 같으면 출력 가능, 그렇지 못하면 출력 불가능

    if num>=c:
        for j in range(num-c+1):
            stack.append(c)
            result.append("+")
            c+=1
        stack.pop()
        result.append("-")
    else:
        if num==stack[-1]:
            stack.pop()
            result.append("-")
        else:
            print("NO")
            flag=1
            break
if flag==0:
    for i in result:
        print(i)
