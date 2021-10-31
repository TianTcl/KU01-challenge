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
const int TT=1e3+2;

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
    freopen("", "r", stdin);
    freopen("", "w", stdout);
}

struct Any { 
    int A,B,C;
    bool operator<(const Any &joox) const {
        return A<joox.A;
    }
};

/* --- Work Space --- */

int main() {
    int n,m,x=0,red[501],blue[501],res=0,neg=0;
    blue[0]=red[0]=0;
    cin >> n >> m;
    for(int i=1;i<=n;i++) cin >> red[i];
    for(int i=1;i<=m;i++) cin >> blue[i];
    for(int i=0;i<=n;i++)
        for(int j=0;j<=m;j++) {
            int q=i%2,c=j%2;
            if(red[i]==blue[j] && q==c) neg++;
        }
    while(x<n) {
        int y=0,syn=x%2;
        while(y<m) {
            if(syn==y%2) {
                if(blue[y]<red[x] && blue[y+1]>red[x+1]) res++;
                else if(blue[y]>red[x] && blue[y+1]<red[x+1]) res++;
            }else {
                if(blue[y+1]>red[x] && blue[y]<red[x+1]) res++;
            }
            y++;
        }
        x++;
    }
    cout << res+neg;
}
/*
Constrains
*/