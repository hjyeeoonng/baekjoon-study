#설탕배달-그리디
for i in range(100):
    
    N=int(input())
    R=0
    if N%5==0:
        R=N//5
    elif N<=9 and N%3==0:
        R=N//3
    elif (N-3)%5==0 and N>=3:
        R=1+(N-3)//5
    elif (N-6)%5==0 and N>=6:
        R=2+(N-6)//5
    elif (N-9)%5==0 and N>=9:
        R=3+(N-9)//5
    elif (N-12)%5==0 and N>=12:
        R=4+(N-12)//5
    else:
        R=-1
    print(R)
