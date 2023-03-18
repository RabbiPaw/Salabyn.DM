import math
D=[[x for x in range(6)] for q in range(6)]
for i in range(6):
    for j in range(6):
        print (i+1,'-',j+1)
        D[i][j]=int(input())
        if D[i][j]==-1:
            D[i][j]=math.inf
Dd=[[x for x in range(6)] for q in range(6)]
for k in range(6):
    for i in range(6):
        for j in range(6):
            Dd[i][j]=min(D[i][k]+D[k][j],D[i][j])
    D=Dd
for i in range(6):
    print(Dd[i])
