# -*- coding: utf-8 -*-
import time
import datetime
print u"--YMDを2進に変換，リバース，日付に戻して同じ物--"
start = time.time()
#例
#19660713
#100101......
#......101001
#19660713

d=datetime.date(1964,10,10)
cont=0
while True:
    d += datetime.timedelta(days = 1)
    if d == datetime.date(2020,7,24):
       break
    date_str = d.strftime('%Y%m%d')
    b = bin(int(date_str)).split('0b')[1]
    rev_date=str(int(b[::-1],2))
    #print rev_date+"::"+date_str
    if(rev_date==date_str):
        print date_str+":"+bin(int(date_str))
        cont+=1
print cont    
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"