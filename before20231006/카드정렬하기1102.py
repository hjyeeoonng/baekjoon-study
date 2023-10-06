from queue import PriorityQueue
que = PriorityQueue()
result=0
        
num=int(input())
for i in range(num):
    que.put(int(input()))

while que.qsize()>1:
    a=que.get()
    b=que.get()
    c=a+b
    result+=c
    que.put(c)

print(result)
