t = int(input())

for _ in range(t):
    n = int(input())
    word1, word2 = input().split()

    if sorted(word1) == sorted(word2):
        print("YES")
    else:
        print("NO")