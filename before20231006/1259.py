import sys
while 1:
    n=sys.stdin.readline().strip()
    if n=='0':
        break
    else:
        if n==n[::-1]:
            print("yes")
        else:
            print("no")

