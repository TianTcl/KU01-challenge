#include <bits/stdc++.h>
#define st first
#define nd second
using namespace std;
int ontop[302]={};
vector <int> saw;
vector <pair<int,int>> ondown;
pair <int,int> box[302];

int main() {
    int n,m,z,mxr,res=0;
    cin >> n >> m;
    for(int i=1;i<=n;i++) {
        int x,y;
        cin >> x >> y;
        box[i]={x,y};
        ondown.push_back({y-x,i});
    }
    sort(ondown.begin(),ondown.end());
    while(m--) {
        cin >> z;
        ontop[z]=1;
    }
    for(auto it:ondown) {
        mxr=0;
        int i=it.nd;
        for(int x=1;x<=n;x++) {
            if(!ontop[x]) continue;
            if(box[i].st<=box[x].st && box[i].nd>=box[x].nd) {
                saw.push_back(x);
            }
        }
        if(saw.size()==1) {
            saw.clear();
            continue;
        }
        for(auto x:saw) ontop[x]=0;
        ontop[i]=saw.size();
        saw.clear();
    }
    for(int i=1;i<=n;i++) {
        if(ontop[i]) {
            res++;
            saw.push_back(i);
        }
    }
    cout << res << '\n';
    for(auto x:saw) cout << x << ' ';
}