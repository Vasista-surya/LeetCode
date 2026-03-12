class Solution {
    public boolean isPalindrome(int x) {
        if(x<0||(x%10==0&& x!=0)){
            return false;
        }
        int rh=0;
        while (x>rh){
            int d=x%10;
            rh=rh*10+d;
            x=x/10;
        }
        return x==rh||x==rh/10;
        
    }
}