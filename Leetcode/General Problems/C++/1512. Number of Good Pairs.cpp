class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int c=0,n=nums.size();
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){ 
                if(nums.at(i)==nums.at(j))
                    c++;
            }
        }
        return c;        
    }
};