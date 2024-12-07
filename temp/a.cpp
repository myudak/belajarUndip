#include <bits/stdc++.h>
using namespace std;

/* clang-format off */

/* TYPES  */
#define ll long long
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi vector<int>
#define vll vector<long long>
#define mii map<int, int>
#define si set<int>
#define sc set<char>

/* FUNCTIONS */
#define itr(i,a,b) for (int i=int(a);i<int(b);i++)
#define f(i,s,e) for(long long int i=s;i<e;i++)
#define cf(i,s,e) for(long long int i=s;i<=e;i++)
#define rf(i,e,s) for(long long int i=e-1;i>=s;i--)
#define pb push_back
#define eb emplace_back


/* UTILS */
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795

/*  All Required define Pre-Processors and typedef Constants */
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int  uint64;


/* clang-format on */

/* Main()  function */
int main()
{
	int N; vector<int> A;
	cin >> N;
	
	int temp;
	while(cin >> temp){
		A.pb(temp);
	}
	
	sort(A.begin(),A.end());
	
	cout << A[N];

	return 0;
    
}
/* Main() Ends Here */