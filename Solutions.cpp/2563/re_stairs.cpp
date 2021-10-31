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
const int TM=1e5+6;
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
    setIn();
    int n,x,y,q,temp;
    ll ram[TM];
    memset(ram,0,sizeof(ram));
    cin >> n >> x;
    temp=x;
    while(--n) {
        cin >> x;
        int k=x;
        if(temp>x) swap(x,temp);
        for(int i=temp+1;i<x;i++) ram[i]++;
        temp=k;
    }
    for(int i=TM-3;i>-1;i-=2) ram[i]+=ram[i+2];
    for(int i=TM-4;i>-1;i-=2) ram[i]+=ram[i+2];
    cin >> q;
    while(q--) {
        cin >> x >> y;
        cout << ram[x%2 ? x+1:x]-ram[y%2 ? y+1:y+2] << ' ';
        cout << ram[x%2 ? x:x+1]-ram[y%2 ? y+2:y+1] << '\n';
    }
}
/*
Constrains
*/