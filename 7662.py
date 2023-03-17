import heapq
import sys
T=int(sys.stdin.readline())
for i in range(T):
    N=int(sys.stdin.readline())
    que=[]
    flag=1#원래 숫자>flag1
    for j in range(N):
        cmd=list(sys.stdin.readline().split())
        cmd[1]=int(cmd[1])
        if cmd[0]=='I':
            heapq.heappush(que,cmd[1]*flag)
        else:
            if len(que)!=0:
                if cmd[1]==-1:#최소삭제
                    if flag==1:#원래라면
                        heapq.heappop(que)
                    else:#원래 아니라면
                        temp=[]
                        while que:
                            t=heapq.heappop(que)
                            temp.append(-t)
                        for i in temp:
                            heapq.heappush(que,i)
                        heapq.heappop(que)
                        flag=1
                else:
                    if flag==-1:
                        heapq.heappop(que)
                    else:
                        temp=[]
                        while que:
                            t=heapq.heappop(que)
                            temp.append(-t)
                        for i in temp:
                            heapq.heappush(que,i)
                        heapq.heappop(que)
                        flag=-1

    if len(que)==0:
        print('EMPTY')
    elif len(que)==1:
        if flag==1:
            print(que[0],que[0])
        else:
            print(-que[0],-que[0])
    else:
        if flag==1:
            resmin=heapq.heappop(que)
            temp=[]
            while que:
                t=heapq.heappop(que)
                temp.append(-t)
            for i in temp:
                heapq.heappush(que,i)
            resmax=heapq.heappop(que)
            print(-resmax,resmin)
        else:
            resmax=heapq.heappop(que)
            temp=[]
            while que:
                t=heapq.heappop(que)
                temp.append(-t)
            for i in temp:
                heapq.heappush(que,i)
            resmin=heapq.heappop(que)
            print(-resmax,resmin)
