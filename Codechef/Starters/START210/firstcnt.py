# cook your dish here
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    indexed_A = []
    for i in range(N):
        indexed_A.append((A[i], i))
        
    indexed_A.sort()

    results = [0] * N
    
    original_index_smallest = indexed_A[0][1]
    results[original_index_smallest] = -1
    
    original_index_largest = indexed_A[N-1][1]
    results[original_index_largest] = -1
    
    for k in range(1, N - 1):
        val_prev = indexed_A[k-1][0]
        val_k = indexed_A[k][0]
        val_next = indexed_A[k+1][0]
        
        original_index = indexed_A[k][1]
        
        mid1 = (val_prev + val_k) // 2
        mid2 = (val_k + val_next) // 2
        
        count = mid2 - mid1
        
        results[original_index] = count
        
    print(' '.join(map(str, results)))