#include <bits/stdc++.h>
#define ll long long
#define pi pair<int,int>
#define pii pair<int,pi>
#define pl pair<ll,ll>
#define st first
#define nd second
using namespace std;
typedef double db;
const int MX=2e9+7;
const int LM=INT_MAX;
const int TM=1e6+2;
const int TT=1e5+3;
const int MOD=1e9+7;
const ll INF=1e18;
const ll UI=1e15;

void setALL(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}
void setIn(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}
void setOut(void) {
    ios_base::sync_with_stdio(false);
    cout.tie(NULL);
}

void print_case(int i) {
    cout << "Case #" << i << ": ";
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
//  ***** Round 4/3 (2564) ***** > URGENT WORK! < - 40/100 -

int main() {
    pair <ll,ll> beg[TT];
    vector <ll> dx,dy;
    double sumx=0,sumy=0;
    ll res=0;
    int n;
    cin >> n;
    for(int i=0;i<n;i++) {
        ll x,y;
        cin >> x >> y;
        beg[i]={x,y};
        dx.push_back(x);
        dy.push_back(y);
    }
    sort(beg,beg+n);
    sort(dx.begin(),dx.end());
    sort(dy.begin(),dy.end());
    if(n&1) {
        sumx=beg[n/2].first*2;
        sumy=beg[n/2].second*2;
    }else {
        sumx=dx[(n/2)-1]+dx[n/2];
        sumy=dy[(n/2)-1]+dy[n/2];
    }
    for(int i=0;i<n;i++) res+=max(abs(sumx-beg[i].first*2),abs(sumy-beg[i].second*2));
    if(n&1) res*=2;
    cout << res;
} 

//Test cases
/*

*/