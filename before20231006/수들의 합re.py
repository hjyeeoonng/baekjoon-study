import sys
for i in range(10):
    
    N=int(sys.stdin.readline())

    result = 0
    i=0
    while (result+i+1)<N:
        i+=1
        result+=i

    if N-result<=i:
        print(i)
    else:
        print(i+1)
#1 1
#2 1
#3 2
#4 2
#5 2
#6 3
#7 3
#8 3
#9 3
#10 4
#11 4
