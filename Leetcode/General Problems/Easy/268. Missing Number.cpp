class Solution
{
public:
    int missingNumber(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        int len = nums.size();
        nums.push_back(1e-6);

        for (int i = 0; i < len + 1; i++)
        {
            if (i != nums[i])
                return i;
        }
        return 0;
    }
};