# -*- coding: utf-8 -*-
print u"両替，すべての組み合わせ"
import itertools
MAX_COUNT=15
coin=[500,100,50,10]
money=1000
c=0
for i in range(2,MAX_COUNT+1):
    for j in itertools.combinations_with_replacement(coin,i):
        if sum(j)==money:
            print j
            c+=1

print "count:"+str(c)