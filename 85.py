import time

ans=0
for i in range(2,2001):
	j=2
	while (i*(i+1)/2)*(j*(j+1)/2)<=2000000:
		rectangles=(i*(i+1)/2)*(j*(j+1)/2)
		if abs(rectangles-2000000)<abs(ans-2000000):
			ans=rectangles
			size=[i,j]
		j+=1

print ans
print size
print size[0]*size[1]

time.sleep(100)
