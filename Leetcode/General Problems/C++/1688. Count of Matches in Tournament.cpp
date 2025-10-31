class Solution {
public:
    int numberOfMatches(int n) {
        int sum = 0,k=n;
        for (int i = 0; i <k; i++)
        {
            if (n % 2 == 0)
            {
                sum += n / 2;
                n = n / 2;
            }
            else
            {
                sum += (n - 1) / 2;
                n = ((n - 1) / 2) + 1;
            }
        }
        return sum;
    }
};