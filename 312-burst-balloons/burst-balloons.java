class Solution {
    public int maxCoins(int[] nums) {
        int n=nums.length;
        int[] arr = new int[n+2];
        arr[0]=1;
        arr[n+1]=1;
        for (int i=0;i<n;i++){
            arr[i+1]=nums[i];
        }
        int[][] dp = new int[n+2][n+2];
        for (int i=2;i<n+2;i++){
            for(int l=0;l<n+2-i;l++){
                int r=l+i;

                for(int k=l+1;k<r;k++){
                    dp[l][r]=Math.max(
                        dp[l][r],dp[l][k]+arr[l]*arr[k]*arr[r]+dp[k][r]
                    );
                }
            }
        }
        return dp[0][n+1];
        
    }
}