import sys
N=int(sys.stdin.readline())
while N != -1:
    #약수 구하기
    num=[]
    flag=N
    for i in range(1,N):
        if i>=flag:
            break
        if N%i==0:
            num.append(i)
            temp=int(N/i)
            if temp!=i:
                num.append(temp)
            flag=temp
    num.sort()
    if sum(num)==N*2:
        t=''
        for i in num[:-1]:
            t+=str(i)+' + '
        t=t[:-3]
        print(N,'= '+t)
    else:
        print(N, 'is NOT perfect.')
    N=int(sys.stdin.readline())
