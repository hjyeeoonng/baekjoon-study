import sys
from collections import deque
carddeq=deque()
num = int(sys.stdin.readline())
for i in range(num):
    carddeq.append(i+1)
while len(carddeq)>1:
    carddeq.popleft()
    c=carddeq.popleft()
    carddeq.append(c)
print(carddeq.pop())
