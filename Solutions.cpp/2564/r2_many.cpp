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
int arr[100001],cep[100001],n,k,p=0,use=0;

int main() {
    ll res=0;
    deque <int> block;
    memset(cep,0,sizeof(cep));
    cin >> n >> k;
    for(int i=0;i<n;i++) cin >> arr[i];
    while(p<n) {
        if(!cep[arr[p]]) use++;
        cep[arr[p]]++;
        while(use>=k) {
            res+=n-p;
            cep[block.front()]--;
            if(cep[block.front()]==0) use--;
            block.pop_front();
        }
        block.push_back(arr[p++]);
    }
    cout << res;
}
//Test cases
/*

*/