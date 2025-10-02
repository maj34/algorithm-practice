n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

distance = []
for idx in range(n-1):
    distance.append(abs(x[idx] - x[idx+1]) + abs(y[idx] - y[idx+1]))

max_idx = distance.index(max(distance))

distance_sum = 0
for idx in range(n-1):
    if idx == max_idx:
        distance_sum += abs(x[idx] - x[idx+2]) + abs(y[idx] - y[idx+2])
    elif idx == max_idx+1:
        continue
    else:
        distance_sum += abs(x[idx] - x[idx+1]) + abs(y[idx] - y[idx+1])

print(distance_sum)