#include<bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int n,k;
	cin >> n >> k;
	int dist[4][n];
	for(int a=0;a<4;a++){
		for(int i=0;i<n;i++){
			cin >> dist[a][i];
		}
	}
	
	
	for(int a=0;a<4;a++){
		sort(dist[a],dist[a]+n);
	}
	
	int res=100000009;
	
	if(k<=n){
			for(int i=0;i<=k;i++){
			int ans=0;
			int num1=i,num2=k-i;
			for(int j=0;j<num1;j++){
				ans=max(ans,dist[0][j]+dist[2][num1-j-1]);
				//cout << dist[0][j] << ", " << dist[2][num1-j-1] << endl;
			}
			for(int j=0;j<num2;j++){
				ans=max(ans,dist[1][j]+dist[3][num2-j-1]);
				//cout << dist[1][j] << ", " << dist[3][num2-j-1] << endl;
			}
			//cout << ans << endl;
			res=min(ans,res);
		}	
	}
	
	else{
		for(int i=0;i<=2*n-k;i++){
			//cout << i << endl;
			int ans=0;
			int num1=k-n+i,num2=n-i;
			for(int j=0;j<num1;j++){
				ans=max(ans,dist[0][j]+dist[2][num1-j-1]);
				//cout << dist[0][j] << ", " << dist[2][num1-j-1] << endl;
			}
			for(int j=0;j<num2;j++){
				ans=max(ans,dist[1][j]+dist[3][num2-j-1]);
				//cout << dist[1][j] << ", " << dist[3][num2-j-1] << endl;
			}
			//cout << ans << endl;
			res=min(ans,res);
		}	
	}
				
	
	/*
	for(int i=0;i<num[0];i++){
		res=max(res,ans[i][0][0]+ans[num[0]-i-1][0][1]);
	}
	for(int i=0;i<num[1];i++){
		res=max(res,ans[i][1][0]+ans[num[1]-i-1][1][1]);
	}
	*/
	cout << res;
	return 0;
}