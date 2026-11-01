class Solution
{
public:
    int minMergedInteger(vector<int> &nums)
    {
        int min = INT_MAX;
        for (int i = 0; i < nums.size(); i += 2)
        {
            int newnum = stoi(to_string(nums[i]) + to_string(nums[i + 1]));
            if (newnum < min)
                min = newnum;
        }
        return min;
    }
}