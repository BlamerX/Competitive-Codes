n = int(input())

solved_problems = 0

for _ in range(n):
    count = sum(map(int, input().split()))

    if count >= 2:
        solved_problems += 1

print(solved_problems)