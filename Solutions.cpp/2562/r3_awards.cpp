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
    int n,x[1000],dat[1000]={},res=MX;
    bool vit[1000];
    memset(vit,false,sizeof(vit));
    x[0]=0;
    vector <int> nice;
    cin >> n;
    for(int i=1;i<=2*n;i++) {
        cin >> x[i];
        if(!x[i]) dat[i]=1;
        else vit[x[i]]=true;
        x[i]+=x[i-1];
        dat[i]+=dat[i-1];
    }
    nice.push_back(0);
    for(int i=1;i<=2*n;i++) if(!vit[i]) nice.push_back(i+nice.back());
    for(int i=n;i<2*n;i++) {
        int temp=(x[i]-x[i-n+1])+nice[dat[i]-dat[i-n+1]];
        res=min(res,temp);
    }
    n=(2*n)*(2*n+1)/2;
    cout << n-res;
}
/*
Constrain
*/