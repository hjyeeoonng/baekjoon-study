import sys

N=int(sys.stdin.readline())
info=[]
preage=0
for i in range(N):
    inn=list(sys.stdin.readline().split())
    preage=inn[0]
    inn[0]=float(inn[0])+(1-(1/(i+1)))
    info.append(inn)

info.sort(key=lambda x : x[0])
for i in info:
    print(int(i[0]),i[1])
