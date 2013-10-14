import time

ans=0
for i in range(1,1000000):
	s=str(i)
	
	bs=bin(i)
	bs=bs[2:]
	
	if s==s[::-1] and bs==bs[::-1]:
		ans=ans+i
		print i

print ans

time.sleep(100)
