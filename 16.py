import time

n=1
for i in range(1000):
	n=n*2
print n

ans = 0
while( n != 0 ):
	ans = ans + n%10
	n=n/10

print ans

time.sleep(100)
