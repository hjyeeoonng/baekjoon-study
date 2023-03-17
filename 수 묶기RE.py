import sys

zerocount=0
onecount=0
result=0
temp=[]
nlist=[]
mlist=[]

N=int(sys.stdin.readline())

for i in range(N):
    innum=int(sys.stdin.readline())
    if innum>1:
        nlist.append(innum)
    elif innum == 0:
        zerocount+=1
    elif innum == 1:
        onecount+=1
    else:
        mlist.append(innum)

nlist.sort()
mlist.sort(reverse=True)
lennlist=len(nlist)
lenmlist=len(mlist)

for i in range(lenmlist):
    temp.append(mlist.pop())
    if len(temp)>1:
        t1=temp.pop()
        t2=temp.pop()
        result+=t1*t2
if len(temp)>0:
    if zerocount<1:
        result+=temp[0]
    else:
        temp=[]

for i in range(lennlist):
    temp.append(nlist.pop())
    if len(temp)>1:
        t1=temp.pop()
        t2=temp.pop()
        result+=t1*t2
if len(temp)>0:
    result+=temp[0]

result+=onecount
print(result)

#절대값이 1보다 큰 음수 두개>서로 곱해서 양수로 만든다.
#음수 3개가 있을 경우 가장 큰 것은 절대값이 큰 거 두개 곱해서 양수로 만들고 남은 하나를 더해서 빼주는 것. 만약 0이 있을 경우 곱해서 0으로 만들어버린다.
#0 음수가 남을 경우 더하고 나머지 경우는 그냥 더해주면 됨
#1 곱하지 말고 무조건 더하기.
#절대값이 2보다 큰 양수 두개> 서로 곱해서 결과값 더하기
