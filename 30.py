import time

ans=0
for i in range(2,1000000):
	s=0
	buffer=i
	
	while buffer!=0:
		s=s+pow(buffer%10,5)
		buffer=buffer/10
	
	if s==i:
		ans=ans+i

print ans


time.sleep(100)