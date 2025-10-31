class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> ans;
        for(int i=0;i<nums.size();i++){
            int freq=nums.at(i);
            int val=nums.at(i+1);
            for(int j=0;j<freq;j++)
                ans.push_back(val);
            i++;
        }
        return ans;
    }
};