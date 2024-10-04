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
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int jumlah_galaksi;
    cin >> jumlah_galaksi;
    
    vector<string> nama_galaksi(jumlah_galaksi);
    vector<vector<pair<string, int>>> koneksi_sementara(jumlah_galaksi);
    
    for(int i=0;i<jumlah_galaksi;i++){
        cin >> nama_galaksi[i];
        int C;
        cin >> C;
        for(int j=0;j<C;j++){
            string tetangga;
            int jarak;
            cin >> tetangga >> jarak;
            koneksi_sementara[i].eb(tetangga, jarak);
        }
    }
    
    vector<pair<string, int>> sorted_nama(jumlah_galaksi);
    
    for(int i=0;i<jumlah_galaksi;i++) sorted_nama[i] = {nama_galaksi[i], i};
    
    sort(sorted_nama.begin(), sorted_nama.end());
    
    auto get_id = [&](const string &s) -> int {
        int left = 0, right = jumlah_galaksi-1, mid;
        while(left <= right){
            mid = left + (right - left)/2;
            if(sorted_nama[mid].first == s) return sorted_nama[mid].second;
            if(sorted_nama[mid].first < s) left = mid +1;
            else right = mid -1;
        }
        return -1;
    };
    vector<vector<pair<int, int>>> adj(jumlah_galaksi, vector<pair<int, int>>());
    for(int i=0;i<jumlah_galaksi;i++) {
        for(auto &[tetangga, jarak] : koneksi_sementara[i]){
            int id_tetangga = get_id(tetangga);
            if(id_tetangga != -1){
                adj[i].eb(id_tetangga, jarak);
            }
        }
    }
    int V;
    cin >> V;
    vector<int> daftar_galaksi(V);
    for(int i=0;i<V;i++){
        string s;
        cin >> s;
        daftar_galaksi[i] = get_id(s);
    }
    int K;
    cin >> K;
    
    const int INF = 1e9;
    vector<int> jarak(jumlah_galaksi, INF);
    vector<int> pred(jumlah_galaksi, -1);
    vector<int> last_seen(jumlah_galaksi, 0);
    int run_id = 0;
    
    auto dijkstra = [&](int sumber, int tujuan) -> pair<int, vector<int>>{
        run_id++;
        priority_queue<pair<int, int>, vector<pair<int, int>>, std::greater<pair<int, int>>> heap;
        jarak[sumber] = 0;
        last_seen[sumber] = run_id;
        heap.emplace(0, sumber);
        while(!heap.empty()){
            auto [current_jarak, u] = heap.top(); heap.pop();
            if(u == tujuan) break;
            if(current_jarak > jarak[u]) continue;
            for(auto &[v, w] : adj[u]){
                if(last_seen[v] != run_id || jarak[u] + w < jarak[v]){
                    jarak[v] = jarak[u] + w;
                    pred[v] = u;
                    last_seen[v] = run_id;
                    heap.emplace(jarak[v], v);
                }
            }
        }
        if(jarak[tujuan] == INF){
            return {0, vector<int>()};
        }
       
        vector<int> path;
        int node = tujuan;
        while(node != -1){
            path.pb(node);
            node = pred[node];
        }
        reverse(path.begin(), path.end());
        int total = jarak[tujuan];
       
        for(auto node_id : path){
            if(last_seen[node_id] == run_id){
                jarak[node_id] = INF;
                pred[node_id] = -1;
            }
        }
        return {total, path};
    };
   
    long long total_goto =0;
    vector<int> jalur_goto;
    if(V >=1){
        jalur_goto.pb(daftar_galaksi[0]);
        for(int i=1;i<V;i++){
            auto [d, path] = dijkstra(daftar_galaksi[i-1], daftar_galaksi[i]);
            total_goto += d;
            if(path.empty()) continue;
            for(int j=1;j<path.size();j++) jalur_goto.pb(path[j]);
        }
    }
   
    long long total_return =0;
    vector<int> jalur_return;
    int terakhir = daftar_galaksi[V-1];
    int awal = daftar_galaksi[0];
    if(terakhir != awal){
        auto [d, path] = dijkstra(terakhir, awal);
        total_return += d;
        if(!path.empty()){
            jalur_return = path;
        }
    }
    else{
        jalur_return.pb(awal);
    }
   
    cout << total_goto << "\n";
    for(int i=0;i<jalur_goto.size();i++){
        cout << nama_galaksi[jalur_goto[i]];
        if(i != jalur_goto.size()-1) cout << " ";
    }
    cout << "\n";
   
    cout << total_return << "\n";
    for(int i=0;i<jalur_return.size();i++){
        cout << nama_galaksi[jalur_return[i]];
        if(i != jalur_return.size()-1) cout << " ";
    }
    cout << "\n";
}

/* Main() Ends Here */