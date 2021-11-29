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
//  ***** Round 5/4 (2564) ***** > URGENT WORK! < - 100/100 -

vector <pair<ll,ll>> pox;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    ll n,m,k,now=1,res;
    cin >> n >> m >> k;
    loop(m) {
        ll x;
        cin >> x;
        pox.push_back({x-1,now});
        now=1-now;
    }
    pox.push_back({n,now});
    res=m;
    while(k--) {
        ll x,y;
        cin >> x >> y;
        pair<ll,ll> tmp={x,-1};
        auto f_1=upper_bound(pox.begin(),pox.end(),tmp)-pox.begin();
        ll you=(f_1>=m+1 ? n+2:pox[f_1].st);
        ll she=(f_1-1<0 ? -1:pox[f_1-1].st);
        ll OH=(you!=n+2 ? pox[f_1].nd:pox[m].nd);
        if(x==n) you=n+2,OH=pox[m].nd;
        if(she<x && x<you && OH!=y) {
            if(x==n) res++;
            else res+=2;
        }
    }
    cout << (m==1 ? 0:res);
} 

//Test cases
/*

*/