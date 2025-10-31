class Solution {
public:
    bool checkValidString(string s) {
        int high = 0, low = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '(')
        {
            high++;
            low++;
        }
        else if (s[i] == ')')
        {
            if (low > 0)
                low--;
            high--;
        }
        else
        {
            if (low > 0)
                low--;
            high++;
        }
        if (high < 0)
            return false;
    }
    return low == 0;
    }
};