#include <iostream>
using namespace std ;

int main()
{
	const int	n = 100 ;
	int		sum[ n+2 ][ n+2 ] = { 0 } ;
	int		buffer = 0 ;
	for( int i = 1 ; i <= n ; i++ )
	{
		for( int j = 1 ; j <= i ; j++ )
		{
			cin >> buffer ;
			sum[ i ][ j ] = max( sum[ i-1 ][ j-1 ], sum[ i-1 ][ j ] ) + buffer ;
		}
	}
	
	cout << *(max_element(sum[n]+1,sum[n]+n+1) ) << endl ;
	
	return 0 ;
}
