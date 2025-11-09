N, M = map(int, input().split())
A = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * (M + 1)
dp[0] = 0

for num in A:
    for s in range(M, -1, -1):
        if dp[s] != INF and s + num <= M:
            dp[s + num] = min(dp[s + num], dp[s] + 1)

print(dp[M] if dp[M] != INF else -1)