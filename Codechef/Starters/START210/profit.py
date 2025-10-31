# cook your dish here
T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    
    total_profit = 0
    
    for i in range(1, N + 1):
        if i > X:
            profit_from_this_customer = i - X
            
            total_profit = total_profit + profit_from_this_customer
            
    print(total_profit)