s=input()
i=0
arr=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
for i in range(len(s)):
    index = ord(s[i])
    index-=97
    if arr[index]==-1:
        arr[index]=i
i=0
for i in range(26):
    print(arr[i],end='')
    print(" ",end='')
