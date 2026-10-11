class Solution
{
public:
    vector<int> maxProductPair(vector<int> &nums, int target)
    {
        int n = nums.size();
        vector<int> res = {-1, -1};
        int maxprod = INT_MIN;

        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (nums[i] + nums[j] == target && nums[i] != nums[j])
                {
                    int prod = nums[i] * nums[j];
                    if (prod > maxprod)
                    {
                        maxprod = prod;
                        if (nums[i] > nums[j])
                            res = {i, j};
                        else
                            res = {j, i};
                    }
                }
            }
        }
        return res;
    }
};