t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    can_win = True
    for i in range(1, n - 1, 2):
        if a[i] != a[i+1]:
            can_win = False
            break
            
    if can_win:
        print("YES")
    else:
        print("NO")