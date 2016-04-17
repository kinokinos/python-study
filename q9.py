# -*- coding: utf-8 -*-
exit()
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
def create_list(s,b,l):
    if b[0]+b[1]==0:
        l.append(s)
        return
    if b[0]!=0:
        create_list(s+"0",[b[0]-1,b[1]],l)
    if b[1]!=0:
        create_list(s+"1",[b[0],b[1]-1],l)
    return l
lists=[]
ll=[]
ll=create_list("",[10,20],[])
#print ll
#for g in itertools.permutations(come, len(come)):
for g in ll:
    cont+=1
    if cont%1000==0:
        print cont
    f=0
    for i in range(1,len(ll)):
        if list(g[:i]).count(1)==list(g[:i]).count(0) \
        and list(g[i:]).count(1)==list(g[i:]).count(0):
            f=1
            check+=1
            break
#    if f==0:
#        cont+=1
print cont
print cont-check

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
