N=int(input())
card=[]
R=0
for i in range(N):
    card.append(int(input()))
while len(card)>1:
    A=card.pop()
    B=card.pop()
    card.append(A+B)
    R+=A+B
print(R)
