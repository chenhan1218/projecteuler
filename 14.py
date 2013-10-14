import time

def chain(n):
	c=0
	while n != 1:
		if n%2==0 :
			n=n/2
		else :
			n=3*n+1
		c=c+1

	return c

ans=0
n=0
for i in range(1,1000001):
	if ans < chain(i):
		ans=chain(i)
		n=i

print n
print ans

time.sleep(100)

