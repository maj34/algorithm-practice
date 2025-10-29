N = int(input())

# Bottom-Up
dp = [0] * (N+1)

for i in range(1, N+1):
    if i <= 2:
        dp[i] = i
    else:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[N]%10007)