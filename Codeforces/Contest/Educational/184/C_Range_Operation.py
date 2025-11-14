t = int(input())
    
results = []
for _ in range(t):
    n = int(input())
    
    a_str= input().split()   
    a = []
    for s_val in a_str:
        a.append(int(s_val))

    P = [0] * (n + 1)
    for i in range(n):
        P[i+1] = P[i] + a[i]

    original_sum = P[n]
    total = original_sum
    max_sum = -1 * (10**19) 

    for k in range(1, n + 1):
        f_k = P[k-1] - (k * k) + k
        if f_k > max_sum:
            max_sum = f_k

        g_k = (k * k) + k - P[k]

        sum = original_sum + max_sum + g_k

        if sum > total:
            total = sum

    results.append(str(total))

print('\n'.join(results))