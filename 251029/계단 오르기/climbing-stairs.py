N = int(input())

# Bottom-Up
# dp = [0, 0, 1, 1] + [0] * (N-3)

# for i in range(4, N+1):
#     dp[i] = dp[i-3] + dp[i-2]

# print(0 if dp[N]==0 else dp[N]%10007)

# Top-Down
memo = [-1] * (N+1)

def stair(N):    
    if memo[N] != -1:
        return memo[N]

    if N <= 1:
        memo[N] = 0
    elif 2 <= N <= 3:
        memo[N] = 1
    else:
        memo[N] = stair(N-3) + stair(N-2)
    return memo[N]

print(0 if stair(N)==0 else stair(N)%10007)