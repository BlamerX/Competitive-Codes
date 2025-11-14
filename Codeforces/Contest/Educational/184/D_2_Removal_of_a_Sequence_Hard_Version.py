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
    step_val = y - 1

    while x > 0 and cur <= limit:
        increment = (cur - 1) // step_val

        if increment == 0:
            break

        target_val = (increment + 1) * step_val
        current_val = cur - 1
        diff = target_val - current_val

        move = (diff + increment - 1) // increment
        if move > x:
            move = x
        cur += move * increment
        x -= move
        
    if cur > limit:
        print(-1)
    else:
        print(cur)