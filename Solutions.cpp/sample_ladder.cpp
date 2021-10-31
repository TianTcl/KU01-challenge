#include <bits/stdc++.h>
#define ll long long
#define pi pair<int,int>
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
    int n,m,x[1002],now=0; x[0]=0;
    cin >> n >> m;
    for(int i=1;i<=n;i++) cin >> x[i];
    while(m--) {
        int toy;
        cin >> toy;
        now+=toy;
        now+=x[max(now,0)];
        now=max(now,0);
        if(now>=n) {
            now=n;
            break;
        }
    }
    cout << now;
}
/*
Constrain
*/