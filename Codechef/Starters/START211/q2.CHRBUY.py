T = int(input())

for _ in range(T):
    W, P, K = map(int, input().split())

    wooden = min(W, K)
    plastic = K - wooden
    total = (wooden * 2) + (plastic * 1)

    print(total)