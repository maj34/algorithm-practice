N = int(input())

# Bottom-Up
dp = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        dp[1] = 2
    elif i == 2:
        dp[2] = 7
    elif i == 3:
        dp[3] = 22
    else:
        dp[i] = dp[i-2]*7 + dp[i-1]*2

print(dp[N]%1000000007)