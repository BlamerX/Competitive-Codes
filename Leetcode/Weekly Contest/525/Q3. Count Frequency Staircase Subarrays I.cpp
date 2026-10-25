class Solution
{
public:
    int countStaircase(vector<int> &nums)
    {
        int res = 0;

        for (int left = 0; left < nums.size(); left++)
        {
            vector<int> order;
            unordered_map<int, int> freq;

            for (int right = left; right < nums.size(); right++)
            {
                int i = nums[right];
                if (freq[i] == 0)
                    order.push_back(i);
                freq[i]++;

                int len = right - left + 1, n = order.size();

                if (len == n * (n + 1) / 2)
                {
                    bool check = true;
                    for (int i = 0; i < n; i++)
                    {
                        if (freq[order[i]] != i + 1)
                        {
                            check = false;
                            break;
                        }
                    }
                    if (check)
                        res++;
                }
            }
        }
        return res;
    }
};