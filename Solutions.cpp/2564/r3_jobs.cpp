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
//  ***** Round 3/2 (2564) ***** > URGENT WORK! < - 100/100 -

int main() {
    int n,x,neg=0,res=0;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> x;
        if(x>18) neg++;
    }
    if(n&1) {
        if(neg>(n>>1)+1) res=2*neg-n-1;
    }else {
        if(neg>(n>>1)) res=2*neg-n-1;
    }
    cout << res+n;
}

//Test cases
/*

*/