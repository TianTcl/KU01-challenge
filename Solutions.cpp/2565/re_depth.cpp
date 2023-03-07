#include<bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int n,q;
	
	int maxLength[50009]={},currentLength[50009]={},currentDepth=0,maxDepth=0;
	
	cin >> n >> q;
	for(int i=0;i<n;i++){
		int d,l;
		cin >> d >> l;
		if(d==-1){
			maxLength[currentDepth]=max(maxLength[currentDepth],currentLength[currentDepth]);
			currentLength[currentDepth]=0;
			//cout << maxLength[currentDepth] << " , " << currentDepth << endl;
		}
		currentDepth+=d;
		maxDepth=max(maxDepth,currentDepth);
		for(int j=1;j<=currentDepth;j++){
			currentLength[j]+=l;
		}
	}
	maxLength[1]=currentLength[1];
	vector<int> maxL;
	for(int i=maxDepth;i>0;i--){
		maxL.push_back(maxLength[i]);
		//cout << maxLength[i] << " ";
	}
	for(int i=0;i<q;i++){
		int ques;
		cin >> ques;
		auto lower = lower_bound(maxL.begin(),maxL.end(),ques);
		cout << maxL.end()-lower << "\n";
	}
	return 0;
}