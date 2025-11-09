N, M = map(int, input().split())
coin = list(map(int, input().split()))

dp = [float('inf')] * (M + 1)
dp[0] = 0

for c in coin:
    for i in range(c, M + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[M] if dp[M] != float('inf') else -1)