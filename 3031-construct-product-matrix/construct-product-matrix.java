class Solution {
    public int[][] constructProductMatrix(int[][] grid) {
        int m=grid.length, n=grid[0].length;
        int s=m*n;
        int mod=12345;

        int[] arr=new int[s];
        int k=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                arr[k++]=grid[i][j]%mod;
            }
        }

        int [] pre=new int[s];
        pre[0]=1;
        for(int i=1;i<s;i++){
            pre[i]=(pre[i-1]*arr[i-1])%mod;
        }
        int[] suf=new int[s];
        suf[s-1]=1;
        for(int i=s-2;i>=0;i--){
            suf[i]=(suf[i+1]*arr[i+1])%mod;
        }
        int[][] r=new int[m][n];
        k=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                r[i][j]=(pre[k]*suf[k])%mod;
                k++;
            }
        }
        return r;
    }
}