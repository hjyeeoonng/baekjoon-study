import sys

def recursion(n):
    if n>1:
        return n*recursion(n-1)
    else:
        return 1

num=int(sys.stdin.readline())

print(recursion(num))
