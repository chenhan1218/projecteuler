import time
from datetime import date

ans=0
for i in range(1901,2001):
	for j in range(1,13):
		if date(i,j,1).weekday()==6:
			ans=ans+1

print ans


time.sleep(100)
