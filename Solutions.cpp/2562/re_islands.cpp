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
    vector <int> res;
    int n,k,x,temp=0,bye=-1,sun=0;
    cin >> n >> k;
    for(int i=1;i<=n;i++) {
        cin >> x;
        if(x<0) temp-=x-1;
        else {
            if(temp!=0) res.push_back(temp);
            if(bye<0) sun++;
            temp=0;
        }
        bye=x;
    }
    if(temp!=0) res.push_back(temp);
    bye=0;
    sort(res.begin(),res.end()); x=res.size();
    for(int i=0;i<x&&sun>k;i++) {
        bye+=res[i];
        sun--;
    }
    cout << bye;
}
/*
Constrins
*/