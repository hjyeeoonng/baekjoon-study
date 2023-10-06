import sys
import heapq
T=int(sys.stdin.readline())
for i in range(T):
    N=int(sys.stdin.readline())
    maxheap=[]
    minheap=[]
    check={}
    length=0
    for j in range(N):
        cmd=list(sys.stdin.readline().split())
        cmd[1]=int(cmd[1])
        if cmd[0]=='I':
            length+=1
            heapq.heappush(minheap,cmd[1])
            heapq.heappush(maxheap,-cmd[1])
            if cmd[1] in check:
                check[cmd[1]]+=1
            else:
                check[cmd[1]]=1
        else:
            if length>0:
                if cmd[1]==-1:
                    res=heapq.heappop(minheap)
                    while check[res]==0:
                        res=heapq.heappop(minheap)
                    check[res]-=1
                else:
                    res=-heapq.heappop(maxheap)
                    while check[res]==0:
                        res=-heapq.heappop(maxheap)
                    check[res]-=1
                length-=1
    if length==0:
        print('EMPTY')
    elif length==1:
        res=heapq.heappop(minheap)
        while check[res]==0:
            res=heapq.heappop(minheap)
        print(res,res)
    else:
        resmax=-heapq.heappop(maxheap)
        while check[resmax]==0:
            resmax=-heapq.heappop(maxheap)
        check[resmax]-=1
        resmin=heapq.heappop(minheap)
        while check[resmin]==0:
            resmin=heapq.heappop(minheap)
        print(resmax,resmin)
        
