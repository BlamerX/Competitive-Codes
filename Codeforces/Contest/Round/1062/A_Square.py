t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    
    if a == b and b == c and c == d:
        print("YES")
    else:
        print("NO")