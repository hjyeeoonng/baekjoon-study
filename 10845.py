import sys
N=int(sys.stdin.readline())
deque=[]
for i in range(N):
    order=sys.stdin.readline().split()
    if order[0]=='push_front':
        deque.insert(0,order[1])
    elif order[0]=='push_back':
        deque.append(order[1])
    elif order[0]=='pop_front':
        if len(deque)>0:
            a=deque.pop(0)
            print(a)
        else:
            print(-1)
    elif order[0]=='pop_back':
        if len(deque)>0:
            a=deque.pop(-1)
            print(a)
        else:
            print(-1)
    elif order[0]=='size':
        print(len(deque))
    elif order[0]=='empty':
        if len(deque)>0:
            print(0)
        else:
            print(1)
    elif order[0]=='front':
        if len(deque)>0:
            print(deque[0])
        else:
            print(-1)
    else:
        if len(deque)>0:
            print(deque[-1])
        else:
            print(-1)
