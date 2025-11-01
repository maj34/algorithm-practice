N = int(input())
lst = [0] + list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
    mn = 0
    for j in range(0, i):
        if lst[i] < lst[j]:
            mn = max(mn, dp[j])
    dp[i] = mn + 1

print(max(dp))