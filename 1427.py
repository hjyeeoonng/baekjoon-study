import sys
text=sys.stdin.readline().strip()
text=list(map(int,text))
text.sort(reverse=True)
for i in text:
    print(i,end='')
