import sys
N,M=map(int,sys.stdin.readline().split())
chess=[]
result=[]
for i in range(N):
    chess.append(sys.stdin.readline().strip())
for i in range(N-8+1):
    for j in range(M-8+1):
        count=0
        if chess[i][j]=='W':
            st='W' #기준이 W
        else:
            st='B' #기준이 B
        count=0
        for m in range(8):
            for n in range(8):
                if (i%2+j%2)%2==((i+m)%2+(j+n)%2)%2 and chess[i+m][j+n]!=st:
                    count+=1
                elif (i%2+j%2)%2!=((i+m)%2+(j+n)%2)%2 and chess[i+m][j+n]==st:
                    count+=1
        result.append(count)
        result.append(64-count)
result.sort()
print(result[0])
