# -*- coding: utf-8 -*-
import re
import time
start = time.time()

print u"--1000~9999で演算子を間に入れて，演算結果を逆順の数値と一致(621 -> 6*21 = 126)，演算子最低一つ--"
print u"+,-,/はいらない．例)999+1=1000"

op=["*",""]
for i in range(1000,10000):
	char=list(str(i))
	#print char
	for op1 in op:
		for op2 in op:
			for op3 in op:
				ans_c= char[0]+op1+char[1]+op2+char[2]+op3+char[3]
				ans_c=re.sub(r'/0', '', ans_c)
				ans_c=re.sub(r'0+(\d+)', '\\1', ans_c)
				ans=eval(ans_c)
				if(str(ans)==str(i)[::-1] and not ans_c.isdigit()):
					print ans_c
					print str(ans)+":"+str(int(str(i)[::-1]))
					#exit()
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
