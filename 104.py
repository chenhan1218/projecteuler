import time
from sets import Set
from datetime import datetime

f1=0
f2=1
k=1

remainder1=0
remainder2=1

print datetime.now()
while 1:
	if len(Set(str(remainder2)+'0'))==10 and len(Set( str(f2)[0:9] + '0' ))==10:
		break
	
	f1=f1+f2
	(f1,f2)=(f2,f1)
	
	remainder1=(remainder1+remainder2)%1000000000
	(remainder1,remainder2)=(remainder2,remainder1)
	k=k+1
	if k%1000==0:
		print k

print k
print remainder2
print datetime.now()

time.sleep(100)

