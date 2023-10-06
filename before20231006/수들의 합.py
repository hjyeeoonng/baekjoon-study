N=int(input())
num=[]
n=1
while N>=0:
    if num.count(N-n)==0 and N-n>0:
        num.append(n)
        N-=n
        n+=1
    else:
        num.append(N)
        break
print(num)
print(len(num))

