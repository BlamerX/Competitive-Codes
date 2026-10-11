class Solution
{
public:
    int numberOfEmployeesWhoMetTarget(vector<int> &hours, int target)
    {
        int sum = 0;
        for (auto it : hours)
        {
            if (it >= target)
                sum += 1;
        }
        return sum;
    }
};