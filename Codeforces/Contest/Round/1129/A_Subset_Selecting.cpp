#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        vector<int> c(n + 2, 0);

        for (int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            c[x]++;
        }

        int s = 0, ans = 0;

        for (int v = 0;; v++)
        {
            s += c[v];
            if (c[v] == 0 || s < (v + 1) * k)
            {
                ans = v;
                break;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}