t = int(input())
for _ in range(t):
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    
    prefix_min1 = [10**9] * (n + 1)
    prefix_max1 = [0] * (n + 1)
    for i in range(1, n+1):
        prefix_min1[i] = min(prefix_min1[i-1], a1[i-1])
        prefix_max1[i] = max(prefix_max1[i-1], a1[i-1])
    
    suffix_min2 = [10**9] * (n + 2)
    suffix_max2 = [0] * (n + 2)
    for i in range(n, 0, -1):
        suffix_min2[i] = min(suffix_min2[i+1], a2[i-1])
        suffix_max2[i] = max(suffix_max2[i+1], a2[i-1])
    
    pairs = []
    for k in range(1, n+1):
        min_val = min(prefix_min1[k], suffix_min2[k])
        max_val = max(prefix_max1[k], suffix_max2[k])
        pairs.append((min_val, max_val))
    
    pairs.sort(key=lambda x: x[0], reverse=True)
    
    INF = 10**9
    g = [INF] * (2*n + 2)
    ptr = 0
    current_min_max = INF
    
    # Process l from 2n down to 1
    for l in range(2*n, 0, -1):
        while ptr < len(pairs) and pairs[ptr][0] >= l:
            current_min_max = min(current_min_max, pairs[ptr][1])
            ptr += 1
        g[l] = current_min_max
    
    ans = 0
    for l in range(1, 2*n+1):
        if g[l] <= 2*n:
            min_r = max(g[l], l)
            if min_r <= 2*n:
                ans += (2*n - min_r + 1)
    
    print(ans)