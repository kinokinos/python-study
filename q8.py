# -*- coding: utf-8 -*-
import time
print u"--YMDを2進に変換，リバース，日付に戻して同じ物--"
start = time.time()
import copy
#例
#19660713
#100101......
#......101001
#19660713

state=[[0,-1],[0,1],[1,0],[-1,0]]
now=[0,0]
cont=0
def search_path(trace,now,time):
    if time ==12:
        global cont
        cont+=1
        return 
    for i in state:
        cont2+=1
        next=[0,0]
        next[0] = now[0] + i[0]
        next[1] = now[1] + i[1]
        if next in trace:
            continue
        else:
            trace2 = copy.deepcopy(trace)
            trace2.append(next)
            search_path(trace2,next,time+1)

'''
for i in range(0,12):
    for j in state:
        next = now + j
        if next.in(trace):
            continue
        else:
            trace.append(next)
            now=next
        if i==11:
            cont+=1
'''
search_path([[0,0]],now,0)
print "count:"+str(cont)    

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"