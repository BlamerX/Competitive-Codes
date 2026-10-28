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
        string s;
        cin >> n >> s;

        int doors = 0, streak = 1;

        for (int i = 1; i < n; i++)
        {
            if (s[i] == s[i - 1])
                streak++;
            else
                streak = 1;

            if (streak == 3)
            {
                doors++;
                streak = 0;
            }
        }
        cout << doors << endl;
    }
    return 0;
}
