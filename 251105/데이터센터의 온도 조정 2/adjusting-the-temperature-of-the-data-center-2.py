N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

max_profit = 0

for T in range(0, 1001):
    total = 0
    for low, high in ranges:
        if T < low:
            total += C
        elif low <= T <= high:
            total += G
        else:
            total += H
    max_profit = max(max_profit, total)

print(max_profit)