class Solution {
public:
    int reverse(int x) {
        long sum=0;
        while(x!=0){
            int res=x%10;
            sum=(sum*10)+res;
            x=x/10; 
        }
        if(x>=INT_MAX || x<=INT_MIN || sum>INT_MAX || sum<INT_MIN)
            return 0;
        else
            return sum; 
    }
};