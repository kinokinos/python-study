# -*- coding: utf-8 -*-
print u"二分カット，ネストの深さ(カット数に制限)"
print u"カットするごとに棒の数が増えていく．\n棒がすべて切り終えると，元の長さを超えるはず．\n人が足りないと，その分しか切れない"

N = 100 #長さ
M = 5 #同時カット数
count=0
def cut(n,m,c):
	'''
	n:長さ
	m:人の数
	c:棒の数
	'''
	print str(n)+":"+str(m)+":"+str(c)
	if n<=c:
		return 0
	elif m<c: #人が足りない
		return cut(n,m,c+m)+1
	else: #普通にカット　長さ半分，人追加，棒二倍
		return cut(n,m,c*2)+1
print cut(N,M,1)