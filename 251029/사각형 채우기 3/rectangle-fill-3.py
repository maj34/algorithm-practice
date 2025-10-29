N = int(input())

MOD = 1000000007
dp = [0] * (N + 1)
sum_dp = [0] * (N + 1)

dp[0] = 1
if N >= 1:
    dp[1] = 2
if N >= 2:
    dp[2] = 7

# 누적합 기저 초기화 (핵심 수정 부분)
sum_dp[0] = dp[0]
if N >= 1:
    sum_dp[1] = (sum_dp[0] + dp[1]) % MOD
if N >= 2:
    sum_dp[2] = (sum_dp[1] + dp[2]) % MOD

for i in range(3, N + 1):
    dp[i] = (2 * dp[i-1] + 3 * dp[i-2] + 2 * sum_dp[i-3]) % MOD
    sum_dp[i] = (sum_dp[i-1] + dp[i]) % MOD

print(dp[N] % MOD)