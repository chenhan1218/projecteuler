import time

f = open('13.txt', 'r')

list=[]

while 1:
	line = f.readline()
	if not line: # i.e. line == EOF
		break
	else:
		list.append(line)

num=[]
for str in list:
	num.append(int(str))

print sum(num)

time.sleep(100)
