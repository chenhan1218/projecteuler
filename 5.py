ans = 1

def gcd( a, b ):
	while( b != 0 ):
		a, b = b, a%b
	return a 

for n in range( 1, 20 + 1 ):
	ans = ans * n / gcd( ans, n )
print ans

