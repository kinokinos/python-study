# -*- coding: utf-8 -*-
import time
print u"--覆面算(READ+WRITE+TALK=SKILL)--"
start = time.time()

import itertools
#READ+WRITE+TALK=SKILL
#R,E,A,D,W,I,T,L,K,S = 10種
#D+E+K%10==L
print "(R, E, A, D, W, I, T, L, K, S)"
#R,W,T,S !=0
c=0
for a in itertools.permutations(range(0,10),10):
    if a[0]==0 or a[4]==0 or a[6]==0 or a[9]==0:
        continue
    elif a[7]==(a[3]+a[1]+a[8])%10:
        read=1000*a[0]+100*a[1]+10*a[2]+a[3]
        write=10000*a[4]+1000*a[0]+100*a[5]+10*a[6]+a[1]
        talk=1000*a[6]+100*a[2]+10*a[7]+a[8]
        skill=10000*a[9]+1000*a[8]+100*a[5]+10*a[7]+a[7]
        if read+write+talk==skill:
            print a
            c+=1
print c
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
