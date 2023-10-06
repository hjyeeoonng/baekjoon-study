import sys
from itertools import combinations
nine=[]
for i in range(9):
    nine.append(int(sys.stdin.readline()))
for i in combinations(nine,2):
    if i[0]+i[1]+100==sum(nine):
        nine.remove(i[0])
        nine.remove(i[1])
        break
for i in nine:
    print(i)
