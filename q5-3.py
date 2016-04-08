# -*- coding: utf-8 -*-
print u"両替，すべての組み合わせ"
print u"再帰"
import itertools
import copy
c=0
def change(money,coins,max):
    global c
    coin = coins.pop(0)
    if len(coins) == 0:
        if money/coin <= max:
            c+=1
    else:
        for i in range(0,(money/coin)+1):
            change(money-coin*i,copy.deepcopy(coins),max-i)
            
change(1000,[500,100,50,10],15)
print "count:"+str(c)