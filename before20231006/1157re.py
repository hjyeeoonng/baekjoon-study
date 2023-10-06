#ord(문자), chr(정수)
import sys
text=sys.stdin.readline()
text=text.upper()
nlist=[]
for i in range(26):
    nlist.append(text.count(chr(i+65)))
max_value=max(nlist)
count=[0]
for i in range(26):
    if nlist[i]==max_value:
        count[0]+=1
        count.append(i)
result=''
if count[0]>1:
    print('?')
else:
    print(chr(count[1]+65))
