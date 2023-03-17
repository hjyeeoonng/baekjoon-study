import sys
N=int(sys.stdin.readline())
for i in range(N):
    print(' '*(N-i-1),end='')
    print('*'*(i*2+1))
for i in range(N-1):
    print(' '*(i+1),end='')
    print('*'*((N-i-2)*2+1))
