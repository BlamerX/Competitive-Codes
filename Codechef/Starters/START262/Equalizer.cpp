#include <bits/stdc++.h>
using namespace std;

int main()
{
    // your code goes here
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<long long> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];

        int score = 0, delta = 0;
        for (int i = 0; i < n - 1; i++)
            if (a[i] == a[i + 1])
                score++;

        vector<int> leftgain(n - 1), rightgain(n - 1);
        for (int i = 0; i < n - 1; i++)
        {
            long long d = a[i] - a[i + 1];
            leftgain[i] = (d == 1) ? +1 : (d == 0 ? -1 : 0);
            rightgain[i] = (d == -1) ? +1 : (d == 0 ? -1 : 0);
        }

        for (int i = 0; i < n - 1; i++)
        {
            delta = max(delta, leftgain[i]);
            delta = max(delta, rightgain[i]);
        }

        if (n >= 3)
        {
            int bestleft = -2;
            for (int i = 1; i < n - 1; i++)
            {
                bestleft = max(bestleft, leftgain[i - 1]);
                delta = max(delta, bestleft + rightgain[i]);
            }
        }

        cout << score + delta << endl;
    }
    return 0;
}
