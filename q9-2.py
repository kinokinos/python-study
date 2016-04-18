# -*- coding: utf-8 -*-
import time
print u"--来た順，振り分け人数・男女を均等に--"
start = time.time()
import itertools
cont=0
def count_binary_permutations(s,b):
    global cont
    #print str(s.count("1"))+"::"+str(s.count("0"))
    if (b[0]==1 and b[1]==0) or (b[0]==0 and b[1]==1):
        cont+=1
        return

    if (s.count("1")>0 or s.count("0")>0) and (s.count("1")==s.count("0") or s.count("1")-10==s.count("0")):
        return
    if b[0]>0:
        count_binary_permutations(s+"0",[b[0]-1,b[1]])
    if b[1]>0:
        count_binary_permutations(s+"1",[b[0],b[1]-1])

count_binary_permutations("",[10,20])
print cont

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
