# -*- coding: utf-8 -*-
import time
print u"--来た順，振り分け人数・男女を均等に--"
start = time.time()
import itertools
#m=20
#f=10
#come=[1]*20 +[0]*10 
#come=[1]*3 +[0]*3 

#print come
lists=[]
cont=0
check=0
#同じ要素を含む順列の生成
l2=[]
def create_list(s,b):
    global cont
    global l2
    #print str(s.count("1"))+"::"+str(s.count("0"))
    if (b[0]==1 and b[1]==0) or (b[0]==0 and b[1]==1):
        cont+=1
        l2.append(s)
        return

    if (s.count("1")>0 or s.count("0")>0) and (s.count("1")==s.count("0") or s.count("1")-10==s.count("0")):
#        print s
#        print str(s.count("1"))+"::"+str(s.count("0"))
        return
    if b[0]>0:
        create_list(s+"0",[b[0]-1,b[1]])
    if b[1]>0:
        create_list(s+"1",[b[0],b[1]-1])

create_list("",[10,20])
#print l2
print len(l2)
print cont

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
