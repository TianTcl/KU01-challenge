#include<bits/stdc++.h>
using namespace std;
bool yes[10000009]={};
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int n,a[105];
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	int res=0;
	for(int i=0;i<n;i++){
		for(int j=i;j<n;j++){
			int cur=0;
			for(int x=i;x<=j;x++){
				cur+=a[x];
			}
			if(!yes[cur]){
				res++;
				yes[cur]=true;
				//cout << "hi" << endl;
			}
		}
	}
	cout << res;
	return 0;
}