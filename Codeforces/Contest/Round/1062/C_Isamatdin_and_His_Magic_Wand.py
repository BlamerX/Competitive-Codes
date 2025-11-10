t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd_count = 0
    for x in a:
        if x % 2 != 0:
            odd_count += 1

    if odd_count == 0 or odd_count == n:
        print(*a)
    else:
        a.sort()
        print(*a)