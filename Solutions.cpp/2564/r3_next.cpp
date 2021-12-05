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
//  ***** Round 3/1 (2564) ***** > URGENT WORK! < - 100/100 -

int dp[TT];
bool vit[TT]={};
int dfs(int k) {
    if(vit[k]) return 0;
    vit[k]=true;
    return 1+dfs(dp[k]);
}

int main() {
    int n,x,res=0;
    cin >> n;
    for(int i=1;i<=n;i++) {
        cin >> x;
        dp[i]=x;
    }
    for(int i=1;i<=n;i++) {
        if(!vit[i]) {
            res=max(res,dfs(i));
        }
    }
    cout << res;
}

//Test cases
/*

*/