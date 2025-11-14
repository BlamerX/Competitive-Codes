from itertools import combinations

t = int(input())

METRICS = [
    (-2, 0), (2, 0),    # -2x - c, 2x - c
    (0, -2), (0, 2),    # -2y - c, 2y - c
    (-2, -2), (-2, 2),  # -2x -2y -c, -2x +2y -c
    (2, -2), (2, 2),    # 2x -2y -c, 2x +2y -c
]

for _ in range(t):
    n = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    cs = list(map(int, input().split()))

    total_cost = sum(cs)

    points = [(xs[i], ys[i], cs[i], i) for i in range(n)]
    cand_indices = set()

    for a, b in METRICS:
        top3 = [(-float('inf'), -1), (-float('inf'), -1), (-float('inf'), -1)]
        
        for x, y, c, idx in points:
            score = a * x + b * y - c

            if score > top3[0][0]:
                top3 = [(score, idx), top3[0], top3[1]]
            elif score > top3[1][0]:
                top3 = [top3[0], (score, idx), top3[1]]
            elif score > top3[2][0]:
                top3 = [top3[0], top3[1], (score, idx)]
        
        for _, idx in top3:
            if idx != -1:
                cand_indices.add(idx)

    cand_data = [(xs[i], ys[i], cs[i]) for i in cand_indices]
    max_adj = -float('inf')
    K = len(cand_data)

    for i in range(K):
        p1 = cand_data[i]
        perimeter = 0 
        cost = p1[2]
        adj = perimeter - cost
        if adj > max_adj:
            max_adj = adj

    # Check subsets of size r = 2
    for i in range(K):
        p1 = cand_data[i]
        for j in range(i + 1, K):
            p2 = cand_data[j]
            min_x = min(p1[0], p2[0])
            max_x = max(p1[0], p2[0])
            min_y = min(p1[1], p2[1])
            max_y = max(p1[1], p2[1])
            cost = p1[2] + p2[2]
            perimeter = 2 * ((max_x - min_x) + (max_y - min_y))
            adj = perimeter - cost
            if adj > max_adj:
                max_adj = adj

    # Check subsets of size r = 3
    for i in range(K):
        p1 = cand_data[i]
        for j in range(i + 1, K):
            p2 = cand_data[j]
            for k in range(j + 1, K):
                p3 = cand_data[k]
                min_x = min(p1[0], p2[0], p3[0])
                max_x = max(p1[0], p2[0], p3[0])
                min_y = min(p1[1], p2[1], p3[1])
                max_y = max(p1[1], p2[1], p3[1])
                cost = p1[2] + p2[2] + p3[2]
                perimeter = 2 * ((max_x - min_x) + (max_y - min_y))
                adj = perimeter - cost
                if adj > max_adj:
                    max_adj = adj
                    
    # Check subsets of size r = 4
    for i in range(K):
        p1 = cand_data[i]
        for j in range(i + 1, K):
            p2 = cand_data[j]
            for k in range(j + 1, K):
                p3 = cand_data[k]
                for l in range(k + 1, K):
                    p4 = cand_data[l]
                    min_x = min(p1[0], p2[0], p3[0], p4[0])
                    max_x = max(p1[0], p2[0], p3[0], p4[0])
                    min_y = min(p1[1], p2[1], p3[1], p4[1])
                    max_y = max(p1[1], p2[1], p3[1], p4[1])
                    cost = p1[2] + p2[2] + p3[2] + p4[2]
                    perimeter = 2 * ((max_x - min_x) + (max_y - min_y))
                    adj = perimeter - cost
                    if adj > max_adj:
                        max_adj = adj

    print(total_cost + max_adj)
