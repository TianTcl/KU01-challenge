#include<bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int n;
	cin >> n;
	int p[n],v[n];
	for(int i=0;i<n;i++){
		cin >> p[i] >> v[i];
	}
	int cur=v[n-1];
	int res=0;
	for(int i=n-2;i>=0;i--){
		if(cur>v[i]){
			res++;
		}
		else{
			cur=v[i];
		}
	}
	cout << res;
	return 0;
}