import sys
N = int(sys.stdin.readline())
student=[]
for i in range(N):
    std = list(map(int,sys.stdin.readline().split()))
    std = list(map(lambda k : k+(200000-std[0])/200001,std))
    student.append(std)
student.sort(key = lambda x : -x[1])
print(int(student[0][0]),end=' ')
del student[0]
student.sort(key = lambda x : -x[2])
print(int(student[0][0]),end=' ')
del student[0]
student.sort(key = lambda x : -x[3])
print(int(student[0][0]),end=' ')
del student[0]
student.sort(key = lambda x : -x[4])
print(int(student[0][0]),end='')
del student[0]
