'''
import sys
T=int(sys.stdin.readline())
for i in range(T):
    H,W,N=map(int,sys.stdin.readline().split())
    
    while N-(H*i)>0:
        i+=1
    floor=N-(H*(i-1))
    ho=i
    if ho<10:
        ho="0"+str(ho)
    print(int(str(floor)+str(ho)))
'''

import sys
T=int(sys.stdin.readline())
for i in range(T):
    H,W,N=map(int,sys.stdin.readline().split())

    ho = N // H + 1
    floor = N % H

    if floor == 0 :
        ho -= 1
        floor= H
        
    if ho<10:
        ho="0"+str(ho)
        
    print(int(str(floor)+str(ho)))
