from queue import PriorityQueue
import sys

N,K=map(int,sys.stdin.readline().split())

result=0

bag=PriorityQueue()
obag=PriorityQueue()
jewel=PriorityQueue()

for i in range(N):
    temp=list(map(int,sys.stdin.readline().split()))
    ntemp=[-temp[1],temp[0]]
    jewel.put(ntemp)
for i in range(K):
    bag.put(int(sys.stdin.readline()))

jlen=jewel.qsize()
blen=bag.qsize()
for i in range(jlen):#보석 모두 하나씩 넣어보자
    jew=jewel.get()
    flag=0
    for j in range(blen):#가방 개수만큼 해보자
        if j%2==0:
            ba=bag.get()
            if jew[1]<=ba:
                if flag==0:
                    result+=(-jew[0])
                    flag=1
                obag.put(-1)
            else:
                obag.put(ba)
        else :
            ba=obag.get()
            if jew[1]<=ba:
                if flag==0:
                    result+=(-jew[0])
                    flag=1
                bag.put(-1)
            else:
                bag.put(ba)
print(result)
