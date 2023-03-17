import sys
N = int(sys.stdin.readline())

count=0
for i in range(100):
    for j in range(100):
        if N-i-j == 0:
            count+=1
print(count)
