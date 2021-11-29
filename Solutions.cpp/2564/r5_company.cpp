#include <bits/stdc++.h>
#define show(x) cerr << #x << " : " << x << '\n'
#define loop(z) for(int i=0;i!=z;i++)
#define all(y) y.begin(),y.end()
#define in(v) cin >> v;
#define out(v) cout << v << '\n';
#define st first
#define nd second
using namespace std;
typedef long long ll;
typedef double db;
typedef float ft;
#define pi pair<int,int>
#define pl pair<ll,ll>
#define pip pair<int,pi>
const int MX=2e9+7;
const int LM=INT_MAX;
const int TM=1e6+2;
const int TT=1e5+3;
const int MOD=1e9+7;
const ll INF=1e18;

void setALL(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}
void print_vec(vector <int> few) {
    for(auto it:few) cout << it << ' ';
    return;
}
void print_case(int i) {
    cout << "Case #" << i << ": ";
    return;
}
template <typename... Y>
void appear_(Y&... var) {
    ((cout << var << ' '), ...);
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
//  ***** Round 5/3 (2564) ***** > URGENT WORK! < - 100/100 -

vector <int> node[TT],own(TT,1);
bool vit[TT]={};

int main() {
    int n,res=0;
    cin >> n;
    for(int i=1,l;i<=n;i++) {
        cin >> l;
        for(int j=0,x,y;j<l;j++) {
            cin >> x >> y;
            if(y>50) node[x].push_back(i);
        }
    }
    queue <int> hx;
    for(int i=1;i<=n;i++) {
        if(!vit[i]) {
            int cnt=0;
            hx.push(i);
            while(!hx.empty()) {
                int v=hx.front();
                hx.pop();

                cnt+=own[v];

                for(auto z:node[v]) {
                    if(!vit[z]) {
                        vit[z]=true;
                        hx.push(z);
                    }
                }
            }
            own[i]=cnt;
            res=max(res,cnt);
        }
    }
    cout << res-1;
} 

//Test cases
/*

*/