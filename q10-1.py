# -*- coding: utf-8 -*-
import time
print u"--n個の連続する数値の最大でeu<usaとなるもの--"
start = time.time()
#高速化、先頭要素を減算、次の要素を加算することで、毎回全部(0~n)を計算しなくてよい

eu=[0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
usa=[0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,00,27,10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2]
cont=0
#2,36
for n in range(2,37):
    usa_cand=0
    for j in range(0,n):
        usa_cand+=usa[j%len(usa)]
    usa_max = usa_cand
    for i in range(0,len(usa)):
        usa_cand += usa[(i+n)%len(usa)]
        usa_cand -= usa[(i)%len(usa)]
        if usa_max < usa_cand:
            usa_max = usa_cand        
    eu_cand=0
    for j in range(0,n):
        eu_cand+=eu[j%len(eu)]
    eu_max = eu_cand
    for i in range(0,len(eu)):
        eu_cand += eu[(i+n)%len(eu)]
        eu_cand -= eu[(i)%len(eu)]
        if eu_max < eu_cand:
            eu_max = eu_cand
    print str(eu_max) +":"+str(usa_max)
    if eu_max < usa_max:
        cont+=1

print cont        
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
