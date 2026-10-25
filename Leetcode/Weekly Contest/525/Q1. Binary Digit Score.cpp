class Solution
{
public:
    int bitcalc(int num)
    {
        int n = 0;
        while (num)
        {
            n += num & 1;
            num = num >> 1;
        }
        return n;
    }

    int calculateScore(int a, int b)
    {
        int s1 = bitcalc(a);
        int s2 = bitcalc(b);

        if (s1 >= s2)
            return s1 * s2;
        if (s1 == 0)
            return 0;
        return s2 / s1;
    }
};