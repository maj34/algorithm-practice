n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_ssum = 0
for i in range(n-k+1):
    ssum = sum(arr[i:i+k])
    max_ssum = max(max_ssum, ssum)

print(max_ssum)