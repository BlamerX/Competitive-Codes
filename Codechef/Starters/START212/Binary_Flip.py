t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    cnt00 = 0
    cnt11 = 0

    for i in range(n - 1):
        if s[i] == '0' and s[i+1] == '0':
            cnt00 += 1
        elif s[i] == '1' and s[i+1] == '1':
            cnt11 += 1

    if cnt11 >= cnt00:
        print(0)
    else:
        diff = cnt00 - cnt11
        ans = (diff + 1) // 2
        print(ans)