class Solution
{
public:
    int minOperations(vector<int> &nums, vector<int> &locked, int k)
    {
        int ans = 0, prefmax = 0;

        for (int i = 0; i < nums.size(); i++)
        {
            if (locked[i] == 1 && (nums[i] != i + 1 || prefmax != i))
            {
                if (k == 0)
                    return -1;
                k--;
                ans++;
                locked[i] = 0;
            }
            if (nums[i] > prefmax)
                prefmax = nums[i];
        }

        for (int i = 0; i < nums.size(); i++)
            if (locked[i] == 0)
                for (int j = i - 1; j >= 0 && locked[j] == 0; j--)
                    if (nums[j] > nums[i])
                        ans++;

        return ans;
    }
};