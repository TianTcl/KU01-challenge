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
//  ***** Round 5/2 (2564) ***** > URGENT WORK! < - 100/100 -

int dx[]={-1,0,1,0},dy[]={0,1,0,-1};

int main() {
    char arr[31][31];
    int n,res=0;
    cin >> n;
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            cin >> arr[i][j];
        }
    }
    queue <pair<pair<int,int>,int>> hx;
    hx.push({{0,0},0});
    while(!hx.empty()) {
        auto o=hx.front();
        hx.pop();

        if(arr[o.st.st][o.st.nd]=='*') continue;

        for(int i=0;i<4;i++) {
            int xx=o.st.st+dx[i],yy=o.st.nd+dy[i];
            if(xx<0 || yy<0 || xx>=n || yy>=n || arr[xx][yy]==arr[o.st.st][o.st.nd] || arr[xx][yy]=='*')
                continue;
            hx.push({{xx,yy},o.nd+1});
        }
        arr[o.st.st][o.st.nd]='*';
    }
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if(arr[i][j]=='*') res++;
        }
    }
    cout << res;
} 

//Test cases
/*

*/