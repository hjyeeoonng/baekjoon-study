import sys
text=sys.stdin.readline().strip()
flag=0
for i in range(int(len(text)/2)):
    if text[i] != text[-(i+1)]:
        flag=1
        break
if flag==1:
    print('0')
else:
    print('1')
