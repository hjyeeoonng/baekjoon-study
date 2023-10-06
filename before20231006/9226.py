import sys
word = sys.stdin.readline().strip()
mo = ['a','e','i','o','u']
while word != '#':
    dokkabi = ''
    w=''
    flag=0
    for i in word:
        if flag == 1:
            dokkabi+=i
        else:     
            if i in mo:
                dokkabi+=i
                flag=1
            else:
                w+=i
    dokkabi+=w
    dokkabi+='ay'
    print(dokkabi)
    word = sys.stdin.readline().strip()
