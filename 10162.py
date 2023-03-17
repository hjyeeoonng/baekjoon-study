import sys
time=int(sys.stdin.readline())
if time%10!=0:
    print(-1)
else:
    A=time//300
    time%=300
    B=time//60
    time%=60
    C=time//10
    time%=10
    print(A,B,C)
