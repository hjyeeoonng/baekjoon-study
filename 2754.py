import sys
n=sys.stdin.readline().strip()
res=0
if n=='F':
    print(0.0)
else:
    if n[0]=='A':
        res=4.0
    elif n[0]=='B':
        res=3.0
    elif n[0]=='C':
        res=2.0
    elif n[0]=='D':
        res=1.0
    if n[1]=='+':
        res+=0.3
    elif n[1]=='0':
        res+=0.0
    else:
        res-=0.3
    print(res)
