t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    zero_or_not = False
    count = 0
    
    for char in s:
        if char == '0':
            zero_or_not = True

        if zero_or_not and char == '1':
            count += 1
            
    print(count)