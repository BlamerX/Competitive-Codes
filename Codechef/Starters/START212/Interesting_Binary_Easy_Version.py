t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    inf = 10**18
    dp = [inf] * 4
        
    for v in range(4):
        if v >= arr[0]:
            dp[v] = v - arr[0]

    for i in range(1, n):
        x = arr[i]
        new_dp = [inf] * 4

        for v in range(4):
            if v >= x:
                cost = v - x

                min_prev = inf
                for u in range(4):
                    if u != v:
                        if dp[u] < min_prev:
                            min_prev = dp[u]
                    
                if min_prev != inf:
                    new_dp[v] = cost + min_prev

        dp = new_dp

    arrns = min(dp)
    print(arrns)