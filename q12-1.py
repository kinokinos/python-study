# -*- coding: utf-8 -*-
import time
print u"--平方根　0~9がすべて現れる数(整数部含むと小数部のみ):Slow edition--"

start = time.time()

import re
f1=False
f2=False
for i in range(2,10000):
    use= i ** 0.5
    chk=list(str(use).replace(".",""))
    chk2=list(re.sub(".*\.","",str(use)))
    if f1==False:
        pool=set()
        for j in chk[:10]:
            pool.add(j)
        if len(pool)==10:
            print i
            f1=True
    if f2==False:
        pool=set()
        for j in chk2[:10]:
            pool.add(j)
        if len(pool)==10:
            print i
            f2=True
    if f1==True and f2==True:
        break
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
