N = int(input())

dp = [0, 0, 1, 1] + [0] * (N-3)

for i in range(4, N+1):
    dp[i] = dp[i-3] + dp[i-2]

print(0 if dp[N]==0 else dp[N]%10007)