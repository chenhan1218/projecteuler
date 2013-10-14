a = 0 
b = 0 
c = 0

for a in range( 1, 1001 ) :
	for b in range( a, 1001 ) :
		c = 1000 - a - b
		if( c <= b ) :
			break
		if( a*a + b*b == c*c ) :
			break
	if( a*a + b*b == c*c ) :
		break

print a*b*c
