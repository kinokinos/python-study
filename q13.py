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
        astr=map(str,a)
        read=astr[0]+astr[1]+astr[2]+astr[3]
        write=astr[4]+astr[0]+astr[5]+astr[6]+astr[1]
        talk=astr[6]+astr[2]+astr[7]+astr[8]
        skill=astr[9]+astr[8]+astr[5]+astr[7]+astr[7]
        if eval(read+"+"+write+"+"+talk)==eval(skill):
            print read+"+"+write+"+"+talk+"=="+skill
            print a
            c+=1
print c
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
