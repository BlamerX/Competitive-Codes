class Solution {
public:
    void leftrotate(string &s, int d)
    {
        reverse(s.begin(), s.begin()+d);
        reverse(s.begin()+d, s.end());
        reverse(s.begin(), s.end());
    }
    bool rotateString(string s, string goal) {
        int n=s.length();
        if(s.length()!=goal.length())
            return false;
        else{
            for(int i=0;i<n;i++){
                leftrotate(goal,1);
                if(s==goal)
                    return true;
            }
        }
        return false;
    }
};