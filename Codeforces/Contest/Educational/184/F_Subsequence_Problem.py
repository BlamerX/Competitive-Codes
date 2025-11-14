MOD = 998244353

row = input().split()
n = int(row[0])
m = int(row[1])
k = int(row[2])

ls = list(map(int, input().split()))

for i in range(k):
    input()

K = [0] * 6
S = 0
for length in ls:
    S += length

    for j in range(1, length + 1):
        if j <= 5: 
            K[j] += 1
            
if S > n:
    print(0)
else:
    N = n - S

    lambdas = [0] * 6

    coff = [0] * 6
    
    lambdas[0] = m % MOD
    coff[0] = 1 
    
    for j in range(1, 6):
        lambdas[j] = (m - j + MOD) % MOD 
        coff[j] = K[j]
        
    inverse = [1] * (N + 1)
    if N >= 2:
        inverse[1] = 1
        for i in range(2, N + 1):
            inverse[i] = (MOD - (MOD // i)) * inverse[MOD % i] % MOD

    g = [0] * (N + 1)
    g[0] = 1

    sums = [0] * 6

    for i in range(1, N + 1):
        numerator = 0
        prev_g = g[i-1]

        for r in range(6):
            val = (lambdas[r] * (prev_g + sums[r])) % MOD
            sums[r] = val

            term = (coff[r] * val) % MOD
            numerator = (numerator + term) % MOD

        g[i] = (numerator * inverse[i]) % MOD

    C = 1
    for j in range(1, 6):
        if K[j] > 0:
            factor = pow(j, K[j], MOD)
            C = (C * factor) % MOD
            
    result = (g[N] * C) % MOD
    print(result)