import time

i=1
digits=''
while len(digits)<1000000 :
	digits=digits+str(i)
	i=i+1

print int(digits[0])*int(digits[9])*int(digits[99])*int(digits[999])*int(digits[9999])*int(digits[99999])*int(digits[999999])

time.sleep(100)
