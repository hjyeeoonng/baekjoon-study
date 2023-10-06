'''
a=input().upper()
na=a.count('A')
nb=a.count('B')
nc=a.count('C')
nd=a.count('D')
ne=a.count('E')
nf=a.count('F')
ng=a.count('G')
nh=a.count('H')
ni=a.count('I')
nj=a.count('J')
nk=a.count('K')
nl=a.count('L')
nm=a.count('M')
nn=a.count('N')
no=a.count('O')
np=a.count('P')
nq=a.count('Q')
nr=a.count('R')
ns=a.count('S')
nt=a.count('T')
nu=a.count('U')
nv=a.count('V')
nw=a.count('W')
nx=a.count('X')
ny=a.count('Y')
nz=a.count('Z')
max_num=max(na,nb,nc,nd,ne,nf,ng,nh,ni,nj,nk,nl,nm,nn,no,np,nq,nr,ns,nt,nu,nv,nw,ny,nz)
print(max_num)

word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])
  '''

a=input().upper()
list1=[['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0],]
for i in range(26):
  list1[i][1]=a.count(list1[i][0].upper())
print(list1)
print("")
