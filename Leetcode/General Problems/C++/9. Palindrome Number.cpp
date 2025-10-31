class Solution {
public:
    bool isPalindrome(int x) {
        long reminder=0,reverse=0,original=abs(x);
        while (x!=0){
            reminder=x%10;
            reverse=reverse*10+reminder;
            x/=10;
        }

        if(original==reverse)
            return true;
        else
            return false;
        
    }
};