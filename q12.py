# -*- coding: utf-8 -*-
import time
print u"--平方根　0~9がすべて現れる数(整数部含むと小数部のみ)--"
start = time.time()
import re    
for i in range(2,10000):
    use= i ** 0.5
    chk=list(str(use).replace(".",""))
    pool=set()
    for j in chk[:10]:
        pool.add(j)
    if len(pool)==10:
        print i
        break
for i in range(2,10000):
    use= i ** 0.5
    chk2=list(re.sub(".*\.","",str(use)))
    pool=set()
    for j in chk2[:10]:
        pool.add(j)
    if len(pool)==10:
        print i
        break
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
