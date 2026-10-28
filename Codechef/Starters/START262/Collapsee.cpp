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

        long long res = 0;
        for (int i = 0; i < n - 2; i++)
            res += abs(a[i]);
        res -= a[n - 2];
        res += a[n - 1];

        cout << res << endl;
    }
    return 0;
}
