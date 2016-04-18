# -*- coding: utf-8 -*-
import time
print u"--フィボナッチの各桁の数を足した数で割り切れるか(小さい順5個)--"
start = time.time()
#21 -> 21/3 --2+1
#144 -> 144/9 --1+4+4
#この次からの5つ

cont=[]
def fibonacci(n,a=1,b=0):
    if n < 1:
        return b
    else:
        return fibonacci(n-1,a+b,a)
i=13
while(True):
    result=fibonacci(i,1,0)
    if result % sum([int(x) for x in list(str(result))]) == 0:
        cont.append(result)
        if len(cont)==5:
            break
    i+=1 
print cont        
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
