import sys
T=int(sys.stdin.readline())
for i in range(T):
    N=int(sys.stdin.readline())
    dic={}
    for i in range(N):
        a,b=sys.stdin.readline().strip().split()
        if b in dic:
            temp=dic[b]
            dic[b]=temp+1
        else:
            dic[b]=1
    #dic완성
    
