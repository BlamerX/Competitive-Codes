class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left=0,n=nums.size();
        for(int i=0;i<n;i++){
            int right=0;
            for(int j=i+1;j<n;j++)
                right+=nums.at(j);
            if(left==right)
                return i;
            left+=nums.at(i);
        }
        return -1;
    }
};