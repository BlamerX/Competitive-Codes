class Solution {
public:
    string replaceDigits(string s) {
        for(int i=1;i<=s.size();i++){
            int c=int(s[i]-'0');
            s[i]=char(s[i-1]+c);
            i++;
        }
        return s;
    }
};