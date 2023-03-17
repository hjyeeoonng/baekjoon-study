import sys
while True:
    stack=[]
    text=sys.stdin.readline()
    text=text[:-1]
    if text=='.':
        break
    for i in text:
        if i in ['(',')','[',']']:
            if len(stack)>0:
                temp=stack.pop()
                if temp=='(' and i==')':
                    continue
                elif temp=='[' and i==']':
                    continue
                else:
                    stack.append(temp)
                    stack.append(i)
            else:
                stack.append(i)
    if len(stack)==0:
        print('yes')
    else:
        print('no')
