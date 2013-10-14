#include <iostream>
#include <string>
using namespace std ;

int	value( const string &a )
{
	int		ret = 1 ;
	for( string::size_type ix = 0 ; ix < a.size() ; ++ix )
	{
		ret *= a[ ix ] - '0' ;
	}
	
	return ret ;
}

int main()
{
	string	all ;
	string	buffer ;
	int		maxValue = 0 ;
	
	while( cin >> buffer )
	{
		all += buffer ;
	}
	
	for( string::size_type ix = 0 ; ix + 5 < all.size() ; ++ix )
		maxValue = max( maxValue, value( all.substr( ix, 5 ) ) ) ;
	
	cout << maxValue << endl ;
	
	return 0 ;
}
