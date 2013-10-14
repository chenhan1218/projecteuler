#include <iostream>
using namespace std ;

int main()
{
	long long int		a = 1 ;
	long long int		b = 2 ;
	long long int		sum = 0 ;
	int		i = 0 ;
	
	while( a <= 4000000 )
	{
		if( a % 2 == 0 )
			sum += a ;
		a += b ;
		swap( a, b ) ;
	}
	
	cout << sum << endl ;
	
	return 0 ;
}
