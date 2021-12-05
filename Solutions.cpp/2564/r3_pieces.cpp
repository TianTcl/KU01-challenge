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
//  ***** Round 3/4 (2564) ***** > URGENT WORK! < - 100/100 -
int dp[TT],cp[TT],ep[TT];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    vector <int> dx,dy;
    int l,w,n,m,q,x,tmp=0;
    cin >> l >> w >> n >> m >> q;
    for(int i=0;i<n;i++) {
        cin >> x;
        if(x-tmp>100000) {
          tmp=x;
          continue;
        }
        if(!dp[x-tmp]) dx.push_back(x-tmp);
        dp[x-tmp]++;
        tmp=x;
    }
    if(l-tmp<=100000) {
        dp[l-tmp]++;
        if(dp[l-tmp]==1) dx.push_back(l-tmp);
    }
    tmp=0;
    for(int i=0;i<m;i++) {
        cin >> x;
        if(x-tmp>100000) {
          tmp=x;
          continue;
        }
        if(!cp[x-tmp]) dy.push_back(x-tmp);
        cp[x-tmp]++;
        tmp=x;
    }
    if(w-tmp<=100000) {
        cp[w-tmp]++;
        if(cp[w-tmp]==1) dy.push_back(w-tmp);
    }
    sort(dx.begin(),dx.end());
    sort(dy.begin(),dy.end());
    for(auto it:dy) {
        for(auto ic:dx) {
            if(it*ic<=100000) ep[it*ic]+=(dp[ic]*cp[it]);
            else break;
        }
    }
    while(q--) {
        cin >> x;
        cout << ep[x] << '\n';
    }
}