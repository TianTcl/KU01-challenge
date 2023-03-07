#include<bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int n;
	cin >> n;
	int col[n],row[n];
	for(int i=0;i<n;i++){
		cin >> row[i];
	}
	for(int i=0;i<n;i++){
		cin >> col[i];
	}
	
	int curCol=0;
	for(int curRow=0;curRow<n;curRow++){
		for(int i=0;i<curCol;i++){
			cout << 0 << " ";
		}
		while(row[curRow]!=0){
			//cout << "hi" << endl;
			if(row[curRow]>=col[curCol]){
				row[curRow]-=col[curCol];
				cout << col[curCol] << " ";
				curCol++;
			}
			else{
				col[curCol]-=row[curRow];
				cout << row[curRow] << " ";
				row[curRow]=0;
			}
		}
		for(int i=0;i<n-curCol-1;i++){
			cout << 0 << " ";
		}
		cout << endl;
	}
	return 0;
}