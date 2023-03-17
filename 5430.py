import sys
from collections import deque
T=int(sys.stdin.readline())
for i in range(T):
    cmd=sys.stdin.readline().strip()
    sys.stdin.readline()
    arr=sys.stdin.readline().strip()
    flag=0
    if len(arr)>2:
        arr=arr[1:-1]
        que=deque(map(int,arr.split(',')))
    else:
        que=deque()
    direction = True
    for j in cmd:
        if j=='D':
            if len(que)>0:
                if direction == True:
                    que.popleft()
                else:
                    que.pop()
            else:
                flag=1
                break
        else:
            direction= not direction
    if flag==0:
        temp=list(que)
        if direction==False:
            temp.reverse()
            psent=''
            psent+='['
            for ad in temp:
                psent+=str(ad)+','
            if psent[-1]==',':
                psent=psent[:-1]
            psent+=']'
            print(psent)
        else:
            psent=''
            psent+='['
            for ad in temp:
                psent+=str(ad)+','
            if psent[-1]==',':
                psent=psent[:-1]
            psent+=']'
            print(psent)
    else:
        print('error')
