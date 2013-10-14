N = 100
a = 0 
b = 0

for n in range( 1, N + 1 ):
	a = a + n * n

b = ( 1 + N ) * N / 2 
b = b * b

print b - a

