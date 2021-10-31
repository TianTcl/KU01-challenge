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
int n,m,res=0;
bool isaw=false;
string k[30];
void check(int x,int y) {
    queue <pi> hx;
    hx.push({x,y});
    while(!hx.empty()) {
        int a=hx.front().st;
        int b=hx.front().nd;
        char wat=k[a][b];
        hx.pop();
        if(wat=='#') continue;
        k[a][b]='#';

        if(wat=='*') res++;
        if(wat=='W') isaw=true;

        if(a>0 && k[a-1][b]!='#') hx.push({a-1,b});
        if(a<n-1 && k[a+1][b]!='#') hx.push({a+1,b});
        if(b>0 && k[a][b-1]!='#') hx.push({a,b-1});
        if(b<m-1 && k[a][b+1]!='#') hx.push({a,b+1});
    }
}

int main() {
    cin >> n >> m;
    for(int i=0;i<n;i++) cin >> k[i];
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(k[i][j]=='A') check(i,j);
        }
    }
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(k[i][j]=='W' && isaw) check(i,j);
        }
    }
    cout << res;
}
/*
Constrins
*/