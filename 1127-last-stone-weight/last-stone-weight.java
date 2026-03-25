class Solution {
    public int lastStoneWeight(int[] stones) {
        int n=stones.length;
        while (n>1){
            Arrays.sort(stones,0,n);
            int y=stones[n-1];
            int x=stones[n-2];
            if(y!=x){
                stones[n-2]=y-x;
            }
            else {
                stones[n-2]=0;
            }
            n--;
        }
        return stones[0];

    }
}