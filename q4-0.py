# -*- coding: utf-8 -*-
print u"二分カット，ネストの深さ"
N = 16
def cut(n,m,c):
	print str(n)+":"+str(m)+":"+str(c)
	if(n-1<=1):
		return 1
	else:
		c+=1
		s=cut(n-m,(n-m)/2,c)
		t=cut(m,m/2,c)
		if(s>t):
			return s+1
		else:
			return t+1

print cut(N,N/2,1)