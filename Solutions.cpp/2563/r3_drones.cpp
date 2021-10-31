#include <bits/stdc++.h>
#define ll long long
#define pi pair<int,int>
#define pii pair<pi,pi>
#define pl pair<ll,ll>
#define st first
#define nd second
using namespace std;
typedef double db;
const int MX=1e9+7;
const int LM=INT_MAX;
const int TM=1e7+2;
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

/* --- Work Space --- */
int main() {
    int n,res,drone=0,use[1002];
    memset(use,0,sizeof(use));
    vector <int> hx;
    cin >> n;
    for(int i=0;i<n;i++) {
        int x;
        cin >> x;
        hx.push_back(x);
    }
    sort(hx.begin(),hx.end(),greater<int>());
    res=0; use[0]=10;
    for(int i=0;i<n;i++) {
        if(use[drone]==10) {
            drone++;
            res+=hx[i]*drone;
            use[drone]++;
        }else if(use[drone]==1) {
            drone++;
            if(use[drone/2]<10) {
                use[drone/2]++;
                res+=hx[i]*drone;
                drone--;
            }else {
                res+=hx[i]*drone;
                use[drone]++;
            }
        }else {
            res+=hx[i]*drone*2;
            use[drone]++;
        }

    }
    cout << res;
}
/*
14
1 1 1 1 1 1 1 2 2 2 2 2 2 2
45
*/