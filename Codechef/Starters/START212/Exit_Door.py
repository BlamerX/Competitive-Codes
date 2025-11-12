
t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    seated = [True] * n
    
    total = 0

    for person in range(n, 0, -1):

        index = -1
        for i in range(n):
            if p[i] == person:
                index = i
                break

        left = 0
        for i in range(0, index):
            if seated[i] == True:
                left += 1

        right = 0
        for i in range(index + 1, n):
            if seated[i] == True:
                right += 1

        if left < right:
            total += left
        else:
            total += right

        seated[index] = False
        
    print(total)