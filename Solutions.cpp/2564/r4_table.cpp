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
//  ***** Round 4/2 (2564) ***** > URGENT WORK! < - 100/100 -
bool vit[101][101]={};

int main() {
    int l,w,n,res=0;
    cin >> l >> w >> n;
    for(int i=0;i<n;i++) {
        int a,b,c,d;
        cin >> a >> b >> c >> d;
        for(int j=a;j<c;j++) {
            for(int k=b;k<d;k++) vit[j][k]=true;
        }
    }
    for(int i=3;i<=l;i++) {
        for(int j=3;j<=w;j++) {
            bool chx=true;
            for(int a=i-3;a<i&&chx;a++) {
                for(int b=j-3;b<j&&chx;b++) {
                    if(vit[a][b]) chx=false;
                }
            }
            if(chx) res++;
        }
    }
    cout << res;
} 

//Test cases
/*

*/