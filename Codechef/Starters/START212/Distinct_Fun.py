t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    seen = set()
    total_operations = 0

    for x in reversed(arr):
        if x in seen:
            total_operations += 1
            seen = {x}
        else:
            seen.add(x)
            
    print(total_operations)