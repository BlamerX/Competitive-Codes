class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int sum=0,n=nums.size();
        vector<int> ans;
        for(int i=0;i<n;i++){
            sum+=nums.at(i);
            ans.push_back(sum);
        }
        return ans;
    }
};