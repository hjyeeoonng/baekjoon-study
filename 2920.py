import sys
text=list(map(int,sys.stdin.readline().split()))
if text==list(range(1,9)):
    print("ascending")
elif text==list(range(8,0,-1)):
    print("descending")
else:
    print("mixed")

