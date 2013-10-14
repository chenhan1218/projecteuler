import time
from fractions import Fraction


for i in range(1,10):
	for j in range(10):
		for k in range(10):
			if j==i or k==i:
				continue
			# calculate four possibles:
			# ij/ik, ij/ki, ji/ik, ji/ ki
			if (10*i+j)<(10*i+k) and (10*i+j)*k==(10*i+k)*j:
				print (10*i+j), (10*i+k)
			if (10*i+j)<(10*k+i) and (10*i+j)*k==(10*k+i)*j:
				print (10*i+j), (10*k+i)
			if (10*j+i)<(10*i+k) and (10*j+i)*k==(10*i+k)*j:
				print (10*j+i), (10*i+k) 
			if (10*j+i)<(10*k+i) and (10*j+i)*k==(10*k+i)*j:
				print (10*j+i), (10*k+i)

print Fraction(16,64)*Fraction(26,65)*Fraction(19,95)*Fraction(49,98)

time.sleep(100)

