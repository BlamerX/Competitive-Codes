class Solution {
public:
    string truncateSentence(string s, int k) {
        string ans="",word;
        istringstream ss(s);
        int cnt=0;
        while (ss >> word)
        {
            if(cnt<k){
                ans+=word;
                if(cnt<k-1)
                    ans+=' ';
            }
            cnt++;
        }
        return ans;
    }
};