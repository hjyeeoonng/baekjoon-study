N=int(input())
rope=[]
for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
for i in range(len(rope)):
    rope[i]*=(i+1)
print(max(rope))
