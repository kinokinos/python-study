# -*- coding: utf-8 -*-
print u"100桁，n番目からn-1個置きにbit反転,0の場所を確認する"
print u"少しシンプルに"
MAX=100
bit= [False] * MAX
for i in range(2,MAX):
		for rev in range(i,MAX,i):
			bit[rev-1]=not(bit[rev-1])

print bit
ans=""
for j in range(0,MAX):
	if bit[j] == 0:
		ans += str(j+1)+","
print "ans:"+ans