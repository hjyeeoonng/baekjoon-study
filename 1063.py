import sys
a,b,c=sys.stdin.readline().split()
c=int(c)
def move(a,cmd):
    for j in cmd:
        if j=='R':
            newpos=chr(ord(a[0])+1)+a[1]
        elif j=='L':
            newpos=chr(ord(a[0])-1)+a[1]
        elif j=='B':
            newpos=a[0]+str(int(a[1])-1)
        else:
            newpos=a[0]+str(int(a[1])+1)
        a=newpos
    return newpos
def check(pos):
    if ord(pos[0])<=ord('H') and ord(pos[0])>=ord('A') and int(pos[1])>=1 and int(pos[1])<=8:
        return True
    else:
        return False
for i in range(c):
    cmd=sys.stdin.readline().strip()
    newpos=move(a,cmd)
    if b==newpos:
        newrpos=move(b,cmd)
        if check(newpos) and check(newrpos):
            a=newpos
            b=newrpos
    else:
        if check(newpos):
            a=newpos
print(a)
print(b)
