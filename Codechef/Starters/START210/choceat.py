# cook your dish here
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    if A != B:
        print(A + B)
    else:
        print((A + B) - 1)