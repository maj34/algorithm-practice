n = int(input())
lst = [int(input()) for _ in range(n)]

import sys
min_distance = sys.maxsize

# 리스트 인덱스 0부터 n-1까지 증가
for idx in range(n):
    distance = 0
    # 곱해지는 값 0, 1, 2, ... n-1
    for mul in range(n):
        distance += lst[(idx+mul)%n] * mul
    if distance < min_distance:
        min_distance = distance

print(min_distance)