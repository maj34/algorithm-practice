n = int(input())
arr = list(map(int, input().split()))

import sys
min_val=sys.maxsize

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[j] - arr[i] < min_val:
            min_val = arr[j]-arr[i]

print(min_val)