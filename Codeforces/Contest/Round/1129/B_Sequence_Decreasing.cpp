#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int mn = INT_MAX;
        for (int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            mn = min(mn, x);
        }
        cout << (mn <= n - 1 ? n : 0) << "\n";
    }
    return 0;
}