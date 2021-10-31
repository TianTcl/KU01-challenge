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
    int n,x[101],y[101],dis[101][101],res=MX;
    cin >> n;
    for(int i=0;i<n;i++) cin >> x[i] >> y[i];
    for(int i=0;i<n;i++) {
        for(int j=i+1;j<n;j++) {
            int temp=abs(x[i]-x[j])+abs(y[i]-y[j]);
            dis[i][j]=dis[j][i]=temp;
        }
    }
    for(int i=0;i<n;i++) {
        for(int j=i+1;j<n;j++) {
            int temp=0;
            for(int k=0;k<n;k++) {
                if(k==i || k==j) continue;
                temp+=min(dis[i][k],dis[j][k]);
            }
            res=min(res,temp);
        }
    }
    cout << (res!=MX ? res:0);
}
/*
Constrain
*/