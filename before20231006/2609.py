import sys
a,b=map(int,sys.stdin.readline().split())
if b>a:
    temp=a
    a=b
    b=temp
def GCD(a,b):
    if a%b==0:
        print(b)
        return b
    else:
        return GCD(b,a%b)
num=GCD(a,b)
print(int(a*b/num))
