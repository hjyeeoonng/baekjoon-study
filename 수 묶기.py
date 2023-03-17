N=int(input())
global R
R=0
ppok=[]
def ppocket(num):
    global R
    pok.append(num)
    if len(ppok)==2:
        a=ppok.pop()
        b=ppok.pop()
        R+=(a*b)
pok=[]
def pocket(num):
    global R
    pok.append(num)
    if len(pok)==2:
        a=pok.pop()
        b=pok.pop()
        R+=(a*b)
m1=[]
zero=[]
numlist=[]
for i in range(N):
    numlist.append(int(input()))
numlist.sort(reverse=True)
for i in range(len(numlist)):
    if numlist[i] > 1:
        ppocket(numlist[i])
    elif numlist[i] < -1:
        pocket(numlist[i])
    elif numlist[i]==-1:
        ml.append(numlist[i])
    elif numlist[i]==0:
        zero.append(numlist[i])
    else:
        R+=numlist[i]
print(R)
