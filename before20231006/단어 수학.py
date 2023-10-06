N=int(input())
num=[]
w={'A': 0,'B': 0,'C': 0,'D': 0,'E': 0,'F': 0,'G': 0,'H': 0,'I': 0,'J': 0,'K': 0,'L': 0,'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,'Y': 0,'Z': 0}
for i in range(N):
    n=input()
    num.append(n)
    weigh=10**(len(n)+1)
    for j in n:
        if j=='A':
            w['A']+=weigh
        elif j=='B':
            w['B']+=weigh
        elif j=='C':
            w['C']+=weigh
        elif j=='D':
            w['D']+=weigh
        elif j=='E':
            w['E']+=weigh
        elif j=='F':
            w['F']+=weigh
        elif j=='G':
            w['G']+=weigh
        elif j=='H':
            w['H']+=weigh
        elif j=='I':
            w['I']+=weigh
        elif j=='J':
            w['J']+=weigh
        elif j=='K':
            w['K']+=weigh
        elif j=='L':
            w['L']+=weigh
        elif j=='M':
            w['M']+=weigh
        elif j=='N':
            w['N']+=weigh
        elif j=='O':
            w['O']+=weigh
        elif j=='P':
            w['P']+=weigh
        elif j=='Q':
            w['Q']+=weigh
        elif j=='R':
            w['R']+=weigh
        elif j=='S':
            w['S']+=weigh
        elif j=='T':
            w['T']+=weigh
        elif j=='U':
            w['U']+=weigh
        elif j=='V':
            w['V']+=weigh
        elif j=='W':
            w['W']+=weigh
        elif j=='X':
            w['X']+=weigh
        elif j=='Y':
            w['Y']+=weigh
        elif j=='Z':
            w['Z']+=weigh
        weigh//=10
nw = sorted(w.items(), key=lambda x: x[1],reverse=True)
count=9
for i in range(26):
    nw[i]=list(nw[i])
    if nw[i][1]!=0:
        nw[i][1]=count
        count-=1
    else:
        nw[i][1]=0
    
R=0
for i in range(len(num)):
    for j in range(26):
        num[i]=num[i].replace(nw[j][0],str(nw[j][1]))
    R+=int(num[i])
print(R)
