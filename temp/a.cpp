#include <bits/stdc++.h>
using namespace std;

/* clang-format off */

/* TYPES  */
#define ll long long
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi vector<int>
#define vs vector<string>
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
int manhattanDistance(int x1, int y1, int x2, int y2) {
    return max(abs(x1 - x2), abs(y1 - y2));
}

int minTime(int R, int C, int K, const vs& grid, const vector<pii>& tr) {
    R--; C--; 

    if (K == 1 && grid[R][C] == '1') return 0;

    vi jarak;
    for (const auto& pos : tr) {
        jarak.push_back(
            (pos.first == R && pos.second == C) ? 0 : manhattanDistance(R, C, pos.first, pos.second)
        );
    }

    sort(jarak.begin(), jarak.end());

    int total = 0;
    for (int i = 0; i < K; i++) {
        total += (jarak[i] * 2);
    } return total;
}

int main() {
    int N, M;
    vs grid;
    vector<pii> trs;

    cin >> N >> M;
    grid.resize(N);

    for (int i = 0; i < N; i++) {
        cin >> grid[i];
        for (int j = 0; j < M; j++) {
            if (grid[i][j] == '1') {
                trs.pb({i, j});
            }
        }
    }
    
    int Q;
    cin >> Q;
    while (Q--) {
        int R, C, K;
        cin >> R >> C >> K;
        cout << minTime(R, C, K, grid, trs) << endl;
    }

    return 0;
}

/* Main() Ends Here */