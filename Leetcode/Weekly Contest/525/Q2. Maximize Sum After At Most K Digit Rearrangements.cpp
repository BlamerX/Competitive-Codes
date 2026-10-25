class Solution
{
public:
    int rearrangedmax(int num)
    {
        string s = to_string(num);
        sort(s.begin(), s.end(), greater<char>());
        return stoi(s);
    }
    long long maximizeSum(vector<int> &nums, int k)
    {
        vector<int> temp = nums;
        long long res = 0;
        vector<long long> gains;

        for (int x : temp)
        {
            res += x;
            gains.push_back(rearrangedmax(x) - x);
        }

        sort(gains.rbegin(), gains.rend());

        for (int i = 0; i < k && i < gains.size(); i++)
        {
            if (gains[i] > 0)
                res += gains[i];
            else
                break;
        }

        return res;
    }
};