import sys

stack=[]

text1=sys.stdin.readline().strip()
text2=sys.stdin.readline().strip()
size=len(text2)

for i in text1:
    stack.append(i)
    if len(stack)>=size and stack[-size:]==list(text2):
        for j in range(size):
            stack.pop()
if stack==[]:
    print('FRULA')
else:
    print(''.join(stack))
