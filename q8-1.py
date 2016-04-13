# -*- coding: utf-8 -*-
import time
print u"--経路探索．同じところを進まず，12ステップで何通り？--"
start = time.time()
import copy
#traceの最後の配列が現在の位置

state=[[0,-1],[0,1],[1,0],[-1,0]]
cont=0
def search_path(trace,time):
    if time ==12:
        global cont
        cont+=1
        return 
    for i in state:
        next=[trace[-1][0] + i[0],trace[-1][1] + i[1]]
        if next in trace:
            continue
        else:
            trace2 = copy.deepcopy(trace)
            trace2.append(next)
            search_path(trace2,time+1)

search_path([[0,0]],0)
print "count:"+str(cont)    

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"