# -*- coding: utf-8 -*-
print u"改造コラッツの予想"
ans=[]
threshold = 10000
for n in range(2,10001,2):
    m=n
    n=n*3+1
    while(True):
        if n%2 == 0:
            n=n/2
        else:
            n=n*3+1
        if n==m:
            ans.append(m)
            break
        elif n==1:
            break
print len(ans)