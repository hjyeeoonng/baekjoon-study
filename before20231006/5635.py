import sys
N=int(sys.stdin.readline())
birthday=[]
for i in range(N):
    name,a,b,c=sys.stdin.readline().split()
    if len(a)<2:
        a='0'+a
    if len(b)<2:
        b='0'+b
    bday=c+b+a
    birthday.append([name,int(bday)])
birthday.sort(key = lambda x : x[1])
print(birthday[-1][0])
print(birthday[0][0])
