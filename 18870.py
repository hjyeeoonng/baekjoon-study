import sys
sys.stdin.readline()
nlist=list(map(int,sys.stdin.readline().split()))
n=nlist[:]
n=set(n)
n=list(n)
n.sort()
for i in nlist:
    lo=0
    hi=len(n)-1
    if n[0]==i:
        print(0,end=' ')
    elif n[-1]==i:
        print(len(n)-1,end=' ')
    else:
        while lo+1<hi:
            mid=(lo+hi)//2
            if n[mid]==i:
                break
            elif n[mid]>i:
                hi=mid
            else:
                lo=mid
        print(mid,end=' ')
