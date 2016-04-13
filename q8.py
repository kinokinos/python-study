# -*- coding: utf-8 -*-
import time
print u"--経路探索．同じところを進まず，12ステップで何通り？--"
start = time.time()
import copy

state=[[0,-1],[0,1],[1,0],[-1,0]]
now=[0,0]
cont=0
def search_path(trace,now,time):
    if time ==12:
        global cont
        cont+=1
        return 
    for i in state:
        next=[0,0]
        next[0] = now[0] + i[0]
        next[1] = now[1] + i[1]
        if next in trace:
            continue
        else:
            trace2 = copy.deepcopy(trace)
            trace2.append(next)
            search_path(trace2,next,time+1)

search_path([[0,0]],now,0)
print "count:"+str(cont)    

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"