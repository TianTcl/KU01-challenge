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
    ll res_1=0,res_2=0;
    int n,s,x;
    cin >> n >> s;
    while(n--) {
        cin >> x;
        if(!(x%3)&&!(x%4)) {
            res_1+=(x/3)*10;
            res_2+=(x/4)*10;
        }
        else if(!(x%3)) {
            res_1+=(x/3)*10;
            res_2+=(x/3)*10;
        }else if(!(x%4)) {
            res_1+=(x/4)*10;
            res_2+=(x/4)*10;
        }
    }
    cout << s-res_1 << ' ' << s-res_2;
}

//Test cases
/*

*/