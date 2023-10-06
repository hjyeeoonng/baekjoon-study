import sys
temp=sys.stdin
flag=0
dic={}
for i in temp:
    if flag==0:
        start,end,ext=str(i).split()
        startm=int(start[-2:])
        starth=int(start[:2])
        endm=int(end[-2:])
        endh=int(end[:2])
        extm=int(ext[-2:])
        exth=int(ext[:2])
        flag=1
    else:
        i=str(i)
        chat=i.split(' ')
        if chat[1] not in dic:
            time=list(map(int,chat[0].split(':')))
            if time[0]<starth or (time[0]==starth and time[1]<=startm):
                a=1
                b=0
            if time[0]<=exth and time[0]>=endh and time[1]<=extm and time[1]>=endm:
                b=1
                a=0
            dic[chat[1]]=[a,b]
        else:
            if time[0]<starth or (time[0]==starth and time[1]<=startm):
                a=dic[chat[1]][0]
                b=dic[chat[1]][1]
                a=1
                dic[chat[1]]=[a,b]
            if time[0]<=exth and time[0]>=endh and time[1]<=extm and time[1]>=endm:
                a=dic[chat[1]][0]
                b=dic[chat[1]][1]
                b=1
                dic[chat[1]]=[a,b]
    
