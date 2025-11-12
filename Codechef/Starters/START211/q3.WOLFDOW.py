T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    
    total_birds = S.count('0')
    eaten_birds = 0
    
    i = 0
    while i < N:
        if S[i] == '1':
            j = i + 1
            while j < N and S[j] == '0':
                eaten_birds += 1
                j += 1
            i = j
        else:
            i += 1
            
    print(total_birds - eaten_birds)