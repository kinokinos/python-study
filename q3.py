# -*- coding: utf-8 -*-
print u"100桁，n番目からn-1個置きにbit反転,0の場所を確認する"
MAX=100
bit= [0] * MAX
for i in range(2,MAX):
		for rev in range(i,MAX,i):
			if bit[rev-1]==0:
				bit[rev-1]=1
			else:
				bit[rev-1]=0

print bit
ans=""
for j in range(0,MAX):
	if bit[j] == 0:
		ans += str(j+1)+","
print "ans:"+ans