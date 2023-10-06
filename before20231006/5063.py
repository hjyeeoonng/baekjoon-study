import sys
N=int(sys.stdin.readline())
for i in range(N):
    a,b,c=map(int,sys.stdin.readline().split())
    if a+c<b:
        print('advertise')
    elif a+c==b:
        print('does not matter')
    else:
        print('do not advertise')
