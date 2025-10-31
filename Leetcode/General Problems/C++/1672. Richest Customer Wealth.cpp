class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        
        vector<int> ans;
        int max=0;
        for(int i=0;i<accounts.size();i++)
            ans.push_back(accumulate((accounts.at(i)).begin(),(accounts.at(i)).end(),0));
        
        for(int i=0;i<ans.size();i++){
            if(max<ans.at(i))
                max=ans.at(i);
        }
        return max;        
    }
};