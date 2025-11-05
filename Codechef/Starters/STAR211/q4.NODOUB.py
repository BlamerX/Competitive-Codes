from collections import Counter

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    counts = Counter(A)
    sorted_keys = sorted(counts.keys(), reverse=True)
    
    K = len(sorted_keys)
    S = 0
    result = []
    idx_largest = 0

    for _ in range(N):
        while idx_largest < K and counts[sorted_keys[idx_largest]] == 0:
            idx_largest += 1
        
        largest_available_key = sorted_keys[idx_largest]
        
        val_to_pick = -1
        
        if largest_available_key != S:
            val_to_pick = largest_available_key
        else:
            idx_next = idx_largest + 1
            while idx_next < K and counts[sorted_keys[idx_next]] == 0:
                idx_next += 1
            
            if idx_next < K:
                val_to_pick = sorted_keys[idx_next]
            else:
                val_to_pick = S
        
        result.append(val_to_pick)
        S += val_to_pick
        counts[val_to_pick] -= 1
        
    print(" ".join(map(str, result)))