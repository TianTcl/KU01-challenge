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
const int TT=1e6+3;
const int MOD=1e9+7;

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
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
}

struct Any { //forgot
    int A,B,C;
    bool operator<(const Any &joox) const {
        return A<joox.A;
    }
};

/* --- Work Space --- */

int main() {
    vector <int> pod;
    int n,k,x,temp=1,neg=0,res=1e8;
    bool boy[302]={};
    cin >> n >> k;
    for(int i=1;i<=n;i++) {
        cin >> x;
        boy[x]=true;
        pod.push_back(x);
    }
    sort(pod.begin(),pod.end());
    for(int i=0;i<n;i++) {
        if(temp!=pod[i]) {
            res=min(res,neg);
            neg=0;
            temp=pod[i];
        }
        neg++;
    }
    res=min(res,neg);
    for(int i=1;i<=k;i++) {
        if(!boy[i]) {
            cout << n;
            return 0;
        }
    }
    cout << n-k*res;
}

//Test cases
/*

*/