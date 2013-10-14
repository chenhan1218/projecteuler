import time
import math

def gcd(a,b):
	while b!=0:
		a%=b
		[a,b]=[b,a]
	return a

solutions =[0]*1001

for m in range(1,1001):
	for n in range(1,m):
		if gcd(m,n)!=1:
			continue
		s=2*m*n+2*m*m
		i=1
		while i*s<=1000:
			solutions[i*s]+=1
			i+=1

print solutions
print max(solutions)
print solutions.index(max(solutions))

time.sleep(100)
