import sys
N=int(sys.stdin.readline())
q1=0
q2=0
q3=0
q4=0
axis=0
for i in range(N):
    x,y=map(int,sys.stdin.readline().split())
    if x==0 or y==0:
        axis+=1
    else:
        if x>0:
            if x*y>0:
                q1+=1
            else:
                q4+=1
        else:
            if x*y>0:
                q3+=1
            else:
                q2+=1
print("Q1: "+str(q1))
print("Q2: "+str(q2))
print("Q3: "+str(q3))
print("Q4: "+str(q4))
print("AXIS: "+str(axis))
