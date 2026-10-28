#include <bits/stdc++.h>
using namespace std;

int main()
{
    // your code goes here
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        string s;
        cin >> n >> k >> s;

        int alarms = 0, i = 0;
        while (i < n)
        {
            if (s[i] == '1')
            {
                int p = min(i + k, n - 1);
                alarms++;
                i = p + 1;
            }
            else
                i++;
        }
        cout << alarms << endl;
    }
    return 0;
}
