class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int> ans;
        int n=encoded.size();
        ans.push_back(first);
        for(int i=0;i<n;i++)
            ans.push_back(encoded.at(i)^ans.at(i));

        return ans;            
    }
};