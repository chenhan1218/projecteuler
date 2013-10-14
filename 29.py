import time
from sets import Set

lis=[];
for i in range(2,101):
	for j in range(2,101):
		lis.append(pow(i,j))

print len(Set(lis))

time.sleep(100)

