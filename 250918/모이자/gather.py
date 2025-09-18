n = int(input())
A = list(map(int, input().split()))

import sys
# min_val = sys.maxsize
min_val = []

for i in range(n):
    distance = 0
    for j in range(n):
        distance += A[j] * abs(j-i)
        # if distance <= min_val:
        #     min_val = distance
    min_val.append(distance)
    # print(distance)

print(min(min_val))