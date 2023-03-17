import sys
j=[]
for i in range(5):
    j.append([i+1,sum(list(map(int,sys.stdin.readline().split())))])
j.sort(key=lambda x : -x[1])
print(j[0][0],j[0][1])
    
