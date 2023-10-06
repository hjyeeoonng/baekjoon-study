List=[0]*10001

def selfnum(num):
    sn=num
    for i in str(num):
        sn+=int(i)
    if sn<10001:
        List[sn]=1

for j in range(1,10001):
    selfnum(j)

List[0]=1
for k in range(len(List)):
    if List[k]==0:
        print(k)
