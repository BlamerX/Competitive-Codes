t = int(input())
    
for _ in range(t):
    s = input()
    n = len(s)

    first_right = n
    for i in range(n):
        if s[i] == '>' or s[i] == '*':
            first_right = i
            break

    last_left = -1

    for i in range(n - 1, -1, -1):
        if s[i] == '<' or s[i] == '*':
            last_left = i
            break

    if first_right < last_left:
        print("-1")
    else:
        time_left = last_left + 1
        time_right = n - first_right
        if time_left > time_right:
            print(time_left)
        else:
            print(time_right)