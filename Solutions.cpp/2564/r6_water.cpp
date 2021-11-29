#include <bits/stdc++.h>
using namespace std;
const int MX=1e7;
//  ***** Round 6/2 (2564) ***** > URGENT WORK! < - 100/100 -

int main() {
    int n,l,x,dp[12][2002]={},now=1;
    cin >> n >> l >> x;
    x/=2;
    dp[0][x]=dp[0][x+1]=1;
    if(x+1==l) dp[0][x]=2,dp[0][x+1]=0;
    if(x==0) dp[0][x+1]=2,dp[0][x]=0;
    for(int i=1;i<n;i++) {
        for(int j=1;j<l+now;j++) {
            if(i&1) dp[i][j]+=dp[i-1][j]+dp[i-1][j-1];
            else {
                if(dp[i-1][j-1]==0 && j==1) dp[i][j]+=dp[i-1][j];
                if(dp[i-1][j+2]==0 && j==l+now-1) dp[i][j]+=dp[i-1][j+1];
                dp[i][j]+=dp[i-1][j]+dp[i-1][j+1];
            }
        }
        now=1-now;
    }
    now=(n&1 ? 0:1);
    for(int i=1;i<l+now;i++) cout << dp[n-1][i] << ' ';
}