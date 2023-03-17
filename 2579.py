import sys

T=int(sys.stdin.readline())
total=[0]*12
for a1 in range(1,4):
    result=a1
    if result<=11:
        total[result]+=1
    for a2 in range(1,4):
        result=a1+a2
        if result<=11:
            total[result]+=1
        for a3 in range(1,4):
            result=a1+a2+a3
            if result<=11:
                total[result]+=1
            for a4 in range(1,4):
                result=a1+a2+a3+a4
                if result<=11:
                    total[result]+=1
                for a5 in range(1,4):
                    result=a1+a2+a3+a4+a5
                    if result<=11:
                        total[result]+=1
                    for a6 in range(1,4):
                        result=a1+a2+a3+a4+a5+a6
                        if result<=11:
                            total[result]+=1
                        for a7 in range(1,4):
                            result=a1+a2+a3+a4+a5+a6+a7
                            if result<=11:
                                total[result]+=1
                            for a8 in range(1,4):
                                result=a1+a2+a3+a4+a5+a6+a7+a8
                                if result<=11:
                                    total[result]+=1
                                for a9 in range(1,4):
                                    result=a1+a2+a3+a4+a5+a6+a7+a8+a9
                                    if result<=11:
                                        total[result]+=1
                                    for a10 in range(1,4):
                                        result=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10
                                        if result<=11:
                                            total[result]+=1
                                        for a11 in range(1,4):
                                            result=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11
                                            if result<=11:
                                                total[result]+=1

for i in range(T):
    N=int(sys.stdin.readline())
    print(total[N])
