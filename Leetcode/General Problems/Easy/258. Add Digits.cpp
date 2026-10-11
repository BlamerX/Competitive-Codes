class Solution
{
public:
    int last(int &num)
    {
        num = (num - num % 10) / 10 + num % 10;
        if (num < 10)
        {
            return num;
        }
        else
        {
            last(num);
        }
        return num;
    }

    int addDigits(int num)
    {
        return last(num);
    }
};