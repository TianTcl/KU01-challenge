#include <bits/stdc++.h>
#define show(x) cerr << #x << " : " << x << '\n'
#define loop(z) for(int i=0;i!=z;i++)
#define all(y) y.begin(),y.end()
#define in(v) cin >> v;
#define out(v) cout << v << '\n';
#define st first
#define nd second
using namespace std;
typedef long long ll;
typedef double db;
typedef float ft;
#define pi pair<int,int>
#define pl pair<ll,ll>
#define pip pair<int,pi>
const int MX=2e9+7;
const int LM=INT_MAX;
const int TM=1e6+2;
const int TT=1e5+3;
const int MOD=1e9+7;
const ll INF=1e18;

void setALL(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}
void print_vec(vector <int> few) {
    for(auto it:few) cout << it << ' ';
    return;
}
void print_case(int i) {
    cout << "Case #" << i << ": ";
    return;
}
template <typename... Y>
void appear_(Y&... var) {
    ((cout << var << ' '), ...);
}

void Finout() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
}

struct Any {
    int A,B,C;
    bool operator<(const Any &joox) const {
        return A<joox.A;
    }
};

/* --- Work Space --- */
//  ***** Round 6/4 (2564) ***** > URGENT WORK! < - 100/100 -

vector <pair<int,int>> pay; 

int main() {
    int n,l,res=0,mix=0,may=MX;
    cin >> n >> l;
    loop(n) {
        int x,y;
        cin >> x >> y;
        pay.push_back({x,min(l,y)});
    }
    sort(pay.begin(),pay.end());
    for(int i=0;i<pay.size();i++) {
        auto x=pay[i];
        mix=max(mix,x.st);
        may=min(may,x.nd);
        if(mix>may) res++,mix=x.st,may=x.nd;
    }
    cout << res+1;
} 

//Test cases
/*

*/