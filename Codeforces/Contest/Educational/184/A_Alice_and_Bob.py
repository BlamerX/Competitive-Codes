t = int(input())

for _ in range(t):
    row = input().split()
    n = int(row[0])
    alice = int(row[1])

    marble_list = list(map(int, input().split()))

    lift = 0
    right = 0
    
    for marble in marble_list:
        if marble < alice:
            lift += 1
        elif marble > alice:
            right += 1
            
    if lift > right:    
        print(alice - 1)
    else:
        print(alice + 1)