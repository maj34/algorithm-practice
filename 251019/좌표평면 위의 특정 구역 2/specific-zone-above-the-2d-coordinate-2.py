n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
min_area = float('inf')

for i in range(n):
    # i번째 점을 제거한 나머지 점들로 min/max 계산
    remaining_x = x[:i] + x[i+1:]
    remaining_y = y[:i] + y[i+1:]

    width = max(remaining_x) - min(remaining_x)
    height = max(remaining_y) - min(remaining_y)
    area = width * height

    min_area = min(min_area, area)

print(min_area)