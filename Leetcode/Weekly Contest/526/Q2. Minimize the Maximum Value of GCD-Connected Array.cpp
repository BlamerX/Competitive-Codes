class Solution
{
public:
    long long minimumMaxValue(int n, int index, int value)
    {
        if (n == 1)
            return value;
        if (value == 1)
            return -1;

        long long store = value;
        for (long long i = 2; i * i <= value; i++)
            if (value % i == 0)
            {
                store = i;
                break;
            }

        if (index > (value - store) / 2)
            return -1;

        long long res = n - 1 - index;

        if (res == 0)
            return value;
        if (value % 2 == 0)
            return value + 2 * res;
        return value + store + 2 * (res - 1);
    }
};