a=[[1,2],[1,5],[1,4],[2,3],[2,4],[2,5],[3,5],[3,6],[4,5],[4,7],[4,8],[5,6],[5,8],[5,9],[7,8],[8,9]]
b=[15,14,23,19,16,15,14,26,25,23,20,24,27,18,14,18]
k=sorted(set(b))
fil=[1,2,3,4,5,6,7,8,9]
s=[]
t=[]
summ=0
while s!=fil:
    for i in k:
        for j in range (len(b)):
            if i==b[j]:
                if len(t)==0:
                    t.append(a[j])
                    summ+=b[j]
                for p in range(len(t)):
                    if len(list(set(t[0])))==len(fil):
                                    s=list(sorted(set(t[0])))
                                    break
                    if a[j][0] not in t[p] and a[j][1] in t[p]:
                        t[p].append(a[j][0])
                        summ+=b[j]
                        break
                    elif a[j][1] not in t[p] and a[j][0] in t[p]:
                        t[p].append(a[j][1])
                        summ+=b[j]
                        break
                    elif a[j][0] not in t[p] and a[j][1] not in t[p]:
                        t.append(a[j])
                        summ+=b[j]
                        break
                    elif a[j][0] in t[p] and a[j][1] in t[p]:
                        break
                print(t)
                print(summ)
                if len(t)>1:
                    for q in range(len(t)):
                        for l in range(len(t[q])):
                            for c in range(1,len(t[q])):
                                if len(list(set(t[q]) & set(t[c])))==1:
                                    for x in t[c]:
                                        t[q].append(x)
                                    t[c]=[]
                                break
print(summ)
