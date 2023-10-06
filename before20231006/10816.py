from collections import Counter
import sys

sys.stdin.readline()
card=list(map(int,sys.stdin.readline().split()))
sys.stdin.readline()
num=list(map(int,sys.stdin.readline().split()))

a=Counter(card)

for i in num:
    if i in a:
        print(a[i],end=' ')
    else:
        print(0,end=' ')
