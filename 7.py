prime = [2]

n = 3

while( len(prime) < 10001 ):
	for i in range( 0, len(prime) ) : 
		if prime[ i ] * prime[ i ] > n  :
			break
		if n % prime[ i ] == 0 :
			break 
	if prime[ i ] * prime[ i ] > n  :
		prime.append( n )
	n = n+1
	

print prime[ len(prime) - 1 ]

