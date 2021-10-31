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
    int A,B,C;
    bool operator<(const Any &joox) const {
        return A<joox.A;
    }
};

/* --- Work Space --- */

int main() {
    int n,b,x,res=0;
    pair<int,int> hook[32];
    cin >> n >> b;
    for(int i=0;i<n;i++) {
        int fi=0,se=1e9;
        for(int j=0;j<n;j++) {
            cin >> x;
            fi=max(fi,x);
            se=min(se,x);
        }
        hook[i]={fi,se};
    }
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if(i==j) res=max(res,hook[i].first-hook[j].second);
            else res=max(res,(hook[i].first+b)-(hook[j].second-b));
        }
    }
    cout << res;
}

//Test cases
/*

*/