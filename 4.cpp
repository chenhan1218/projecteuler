#include <iostream>
using namespace std ;

string itoa( long long int a )
{
	string	str ;
	do
	{
		str.insert( 0, 1, '0' + a%10 ) ;
		a /= 10 ;
	} while( a != 0 ) ;
	return str ;
}

bool isPalindrome( long long int a )
{
	string	str = itoa( a ) ;
	int		i = 0 ;
	for( i = 0 ; i*2 < str.size() ; i++ )
	{
		if( str[ i ] != str[ str.size() - 1 - i ] )
			return false ;
	}
	
	return true ;
}

int main()
{
	long long int	i = 0 ;
	long long int	j = 0 ;
	long long int	ans = 0 ;
	
	for( i = 100 ; i <= 999 ; i++ )
	{
		for( j = 100 ; j <= 999 ; j++ )
		{
			if( isPalindrome( i*j ) == true )
				ans = max( ans, i*j ) ;
		}
	}
	
	cout << ans << endl ;
	
	return 0 ;
}
