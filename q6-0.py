# -*- coding: utf-8 -*-
print u"コラッツの予想"
N = 184 #初期値
c = 0 
threshold = 1000
while(True):
    if N%2 == 0:
        N=N/2
    else:
        N=N*3+1
    c+=1

    if N==1:
        print "END"
        break

    if c > threshold:
        print "NOT GOOD"
        break