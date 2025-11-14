t = int(input())

for _ in range(t):
    row = input().split()
    x = int(row[0])
    y = int(row[1])
    k = int(row[2])

    if y == 1:
        print(-1)
        continue

    cur = k
    limit = 10**12 
    possible = True

    for step in range(x):
        cur = cur + (cur - 1) // (y - 1)

        if cur > limit:
            possible = False
            break

    if possible:
        print(cur)
    else:
        print(-1)