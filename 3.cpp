#include <iostream>
using namespace std ;

int main()
{
	long long int		a = 600851 ;
		a = a * 1000000 + 475143 ;
	long long int		i = 0 ;
	
	for( i = 2 ; i <= a ; i++ )
	{
		while( a % i == 0 )
		{
			a /= i ;
		}
	}
	
	cout << i-1 << endl ;
	
	return 0 ;
}
