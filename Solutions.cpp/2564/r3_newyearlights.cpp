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
//  ***** Round 3/3 (2564) ***** > URGENT WORK! < - 100/100 -
vector <int> graph[TT],mad;
vector <vector<int>> node[TT];
bool vit[TT]={};

int main() {
    int n,m,x,res=0;
    cin >> n >> m;
    while(m--) {
        int k,t;
        cin >> k;
        vector <int> stax;
        while(k--) {
            cin >> x;
            stax.push_back(x);
        }
        cin >> t;
        for(auto it:stax) graph[it].push_back(t);
        node[t].push_back(stax);
        mad.push_back(t);
    }
    queue <int> hx;
    hx.push(1);
    while(!hx.empty()) {
        int ux=hx.front();
        hx.pop();

        if(vit[ux]) continue;
        vit[ux]=true;
        res++;

        for(auto it:graph[ux]) {
            if(!vit[it]) {
                for(auto a:node[it]) {
                    bool chx=true;
                    for(auto r:a) if(!vit[r]) chx=false;
                    if(chx) {
                        hx.push(it);
                        break;
                    }
                }
            }
        }
    }
    cout << res;
} 

//Test cases
/*

*/