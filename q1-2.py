# -*- coding: utf-8 -*-

print u"--2,8,10進数で回文，10以上で最小の値--"
#2進数で回文
#1001
#0110 <- 先頭が0は発生しない(偶数は考えなくてよい)
#1111
#
i = 11
while True:
	b = bin(i)
	x = oct(i)
	b = b.split('0b')[1]
	x = x.split('0')[1]
	if str(i) == str(i)[::-1] and b==b[::-1] and x==x[::-1] :
		print "succeed"
		print "ans="+str(i)
		break
	i+=2
