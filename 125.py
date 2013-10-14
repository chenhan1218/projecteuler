import time
from sets import Set

list=[]
for i in range(1,10000):
	s=i*i
	for j in range(i+1,10000):
		s=s+j*j
		if s >= 100000000:
			break
		string=str(s)
		if string==string[::-1]:
			list.append(s)

list=Set(list)
print sum(list)

time.sleep(100)
