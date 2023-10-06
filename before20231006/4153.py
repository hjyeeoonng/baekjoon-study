import sys
while 1:
    a,b,c=map(int,sys.stdin.readline().split())
    if a+b+c==0:
        break
    else:
        if b>a:
            a,b=b,a
        if c>a:
            c,a=a,c
        if c*c+b*b==a*a:
            print("right")
        else :
            print("wrong")
