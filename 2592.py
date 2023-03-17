import sys
from collections import Counter
num=[]
for i in range(10):
    num.append(int(sys.stdin.readline()))
print(sum(num)//10)
print(Counter(num).most_common(1)[0][0])
