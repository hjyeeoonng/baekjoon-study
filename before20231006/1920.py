import sys
N=int(sys.stdin.readline())
A=list(sys.stdin.readline().strip().split())
M=int(sys.stdin.readline())
num=list(sys.stdin.readline().strip().split())
A.sort()
def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start+end)//2

        if data[mid] == target:
            print('1')
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid-1
    print('0')
    return 0
for i in num:
    binary_search(i,A)
