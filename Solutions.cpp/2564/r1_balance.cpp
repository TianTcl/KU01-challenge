#include <bits/stdc++.h>
#define ll long long
#define pi pair<int,int>
#define pii pair<pi,pi>
#define pl pair<ll,ll>
#define st first
#define nd second
using namespace std;
typedef double db;
const int MX=2e9+7;
const int LM=INT_MAX;
const int TM=1e5+2;
const int TT=1e6+3;
const int MOD=1e9+7;

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

struct Any { //forgot
    int A,B,C,D;
    bool operator<(const Any &joox) const {
        return A<joox.A;
    }
};

/* --- Work Space --- */
Any kan[1001];
int n,res=0;
int dfs(Any down) {
    int l,r;
    if(!down.A) l=dfs(kan[down.B]);
    else l=down.B;
    if(!down.C) r=dfs(kan[down.D]);
    else r=down.D;
    res+=abs(l-r);
    return 2*max(l,r);
}

int main() {
    cin >> n;
    for(int i=1;i<=n;i++) {
        int a,l,b,r;
        cin >> a >> l >> b >> r;
        kan[i]={a,l,b,r};
    }
    dfs(kan[1]);
    cout << res;
}

//Test cases
/*

*/