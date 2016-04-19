# -*- coding: utf-8 -*-
import time
print u"--覆面算(READ+WRITE+TALK=SKILL):Generalization,slow--"
start = time.time()

import itertools
import re
import string

def dict_value_check(d,l,chk):
    f=False
    for i in l:
        if d[i]==chk:
            f=True
    return f

#READ+WRITE+TALK=SKILL
question="READ+WRITE+TALK==SKILL"
question="We * love == CodeIQ"

nums=re.split("[^a-zA-Z]*",question) #単語
chars = list(set(''.join(nums))) #アルファベット
head = [s[0] for s in nums] #アルファベットの先頭
c=0

for a in itertools.permutations(range(0,10),len(chars)):
    f=0
    for index,i in enumerate(a):
        if i == 0 and chars[index] in head:
            f=1
    if f==1:
        continue
    e=question.translate(string.maketrans("".join(chars),"".join([str(i) for i in a])))
    if eval(e):
        print e
        print a
        c+=1
print c
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
