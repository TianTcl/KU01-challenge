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
    int n,res=0;
    cin >> n;
    string k[n];
    for(int i=0;i<n;i++) cin >> k[i];
    queue <pi> bot;
    bot.push({n-1,n-1});
    while(!bot.empty()) {
        int a=bot.front().first;
        int b=bot.front().second;
        bot.pop();
        if(k[a][b]=='X') continue;
        k[a][b]='X';
        res++;

        if(a>0) bot.push({a-1,b});
        if(b>0) bot.push({a,b-1});
    }
    cout << res;
}

//Test cases
/*

*/