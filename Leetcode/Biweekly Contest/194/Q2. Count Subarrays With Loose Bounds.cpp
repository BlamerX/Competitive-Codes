class Solution
{
public:
    long long countSubarrays(vector<int> &nums, int minK, int maxK)
    {
        long long res = 0, len = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] >= minK && nums[i] <= maxK)
                len++;
            else
            {
                res += len * (len + 1) / 2;
                len = 0;
            }
        }
        res += len * (len + 1) / 2;
        return res;
    }
};