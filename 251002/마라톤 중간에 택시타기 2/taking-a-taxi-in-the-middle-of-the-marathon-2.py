n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# distance = []
# for idx in range(n-1):
#     distance.append(abs(x[idx] - x[idx+1]) + abs(y[idx] - y[idx+1]))

# max_idx = distance.index(max(distance))

# distance_sum = 0
# for idx in range(n-1):
#     if idx == max_idx:
#         distance_sum += abs(x[idx] - x[idx+2]) + abs(y[idx] - y[idx+2])
#     elif idx == max_idx+1:
#         continue
#     else:
#         distance_sum += abs(x[idx] - x[idx+1]) + abs(y[idx] - y[idx+1])

# print(distance_sum)

import sys

# 맨해튼 거리를 계산하는 함수
def dist(p1_idx, p2_idx):
    x1, y1 = points[p1_idx]
    x2, y2 = points[p2_idx]
    return abs(x1 - x2) + abs(y1 - y2)

# 1. 먼저 아무것도 건너뛰지 않았을 때의 총 거리를 계산
total_distance = 0
for i in range(n - 1):
    total_distance += dist(i, i + 1)

max_saved_distance = 0

# 2. 2번부터 N-1번 체크포인트(인덱스로는 1부터 n-2)를 건너뛰는 경우를 모두 시도
for i in range(1, n - 1):
    # i를 건너뛰면 (i-1 -> i -> i+1) 경로가 (i-1 -> i+1)로 바뀜
    original_path_dist = dist(i - 1, i) + dist(i, i + 1)
    shortcut_dist = dist(i - 1, i + 1)
    
    saved_distance = original_path_dist - shortcut_dist
    
    # 가장 많이 절약되는 거리를 갱신
    if saved_distance > max_saved_distance:
        max_saved_distance = saved_distance

# 3. 최종 결과 = 총 거리 - 가장 많이 절약된 거리
min_distance = total_distance - max_saved_distance
print(min_distance)