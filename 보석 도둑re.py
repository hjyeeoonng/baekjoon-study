from queue import PriorityQueue
import sys

result=0
flag=0
que=PriorityQueue()
N,K=map(int,sys.stdin.readline().split())
jewel=[]
bag=[]
for i in range(N):
    jewel.append(list(map(int,sys.stdin.readline().split())))
for i in range(K):
    bag.append(int(sys.stdin.readline()))

jewel.sort(key=lambda x:-x[1])
bag.sort()

for i in range(N):
    que.put((i,jewel[i]))#정렬해서 우선순위 큐에 넣기(비싼게 우선순위가 높음)

for i in range(que.qsize()):  
    bjewel=que.get()
    for j in range(len(bag)):
        if bag[j]>=bjewel[1][0]:
            result+=bjewel[1][1]
            bag[j]=0
            flag=1
            break
    if flag==1:
        bag.remove(0)
        flag=0

print(result)
