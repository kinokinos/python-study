# -*- coding: utf-8 -*-
import time
print u"--覆面算(READ+WRITE+TALK=SKILL):Generalization,slow--"
start = time.time()

import itertools
import re
import string
import copy
country=["Brazil","Croatia","Mexico","Cameroon","Spain","Netherlands","Chile","Austaralia","Colombia","Greece","Coted'lvoire","Japan","Uruguay","Costa Rica","England","Italy","Switzerland","Ecuador","France","Honduras","Argentina","Bosnia and Herzegovina","Iran","Nigeria","Germany","Portugal","Ghana","USA","Belgium","Algeria","Russia","Korea Republic"]
def shiritori(cont,route,s):
    ans=len(route)
    candidate=route[:]
    for c in list(set(cont)-set(route)):
        if c[0]==s.upper():
            cand = shiritori(cont,route+[c],c[-1])
            if len(cand) > ans:
                ans = len(cand)
                candidate=cand
    return candidate

ans=[]
for i in range(ord('a'),ord('z')+1):
    cand=shiritori(country,[],chr(i))
    if len(cand) > len(ans):
        ans=cand
print ans
print len(ans)
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
