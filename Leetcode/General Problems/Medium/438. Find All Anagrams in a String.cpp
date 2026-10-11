class Solution
{
public:
    vector<int> findAnagrams(string s, string p)
    {
        double sum1 = 0;
        vector<int> res;

        if (s.size() < p.size())
            return res;

        for (int i = 0; i <= p.size(); i++)
            sum1 += sqrt(p[i]);

        for (int i = 0; i <= (s.size() - p.size()); i++)
        {
            double sum2 = 0;
            for (int j = i; j < p.size(); j++)
            {
                sum2 += sqrt(s[j]);
            }
            if (fabs(sum1 - sum2) < 1e-4)
            {
                res.push_back(i);
            }
        }

        return res;
    }
};