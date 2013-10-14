import time
f1=0;
f2=1;
n=1;

while len(str(f2))<1000:
	buffer=f1+f2;
	f1=f2;
	f2=buffer;
	n=n+1

print f2
print n

time.sleep(100)