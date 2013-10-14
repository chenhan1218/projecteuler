import time

def fact(x):
	if x==0 :
		return 1
	else :
		return x * fact(x-1)

def c(x,y):
	return fact(x)/fact(y)/fact(x-y)

count=0
for i in range(1,101):
	for j in range(1,i+1):
		if c(i,j) > 1000000:
			count=count+1

print count

time.sleep(100)

