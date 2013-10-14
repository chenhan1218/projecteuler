import time

n=1
for i in range(1,101):
	n=n*i
print n

ans = 0
while( n != 0 ):
	ans = ans + n%10
	n=n/10

print ans

time.sleep(100)
