import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = sum(arr)
min_diff = sys.maxsize

for i in range(N):
    for j in range(i, N):
        min_diff = min(min_diff, abs(S - (arr_sum - arr[i] - arr[j])))

print(min_diff)