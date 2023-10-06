import sys
from collections import Counter
N=int(sys.stdin.readline())
num=[]
for i in range(N):
    num.append(int(sys.stdin.readline()))
sansul=sum(num)/len(num)
print(round(sansul))
num.sort()
mid=len(num)//2
print(num[mid])#중앙값 출력
c = Counter(num)
order = c.most_common()
maximum = order[0][1]
modes = []
for n in order:
    if n[1] == maximum:
        modes.append(n[0])
if len(modes)>1:
    modes.sort()
    print(modes[1])
else:
    print(modes[0])
print(max(num)-min(num))#범위 출력
