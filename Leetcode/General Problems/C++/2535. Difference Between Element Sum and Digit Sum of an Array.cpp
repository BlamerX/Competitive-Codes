class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int sum1=0,sum2=0,n=nums.size();
        for(int i=0;i<n;i++){
            sum1+=nums[i];
            while(nums[i]>0){
                sum2+=nums[i]%10;
                nums[i]/=10;
            }
        }      
        return abs(sum1-sum2);
    }
};