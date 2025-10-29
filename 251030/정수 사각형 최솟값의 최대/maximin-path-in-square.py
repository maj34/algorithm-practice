N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

dp[0][0] = grid[0][0]

for i in range(1, N):
    dp[0][i] = min(dp[0][i-1], grid[0][i])

for j in range(1, N):
    dp[j][0] = min(dp[j-1][0], grid[j][0])

for i in range(1, N):
    for j in range(1, N):
        min_from_up = min(dp[i-1][j], grid[i][j])        
        min_from_left = min(dp[i][j-1], grid[i][j])
        
        dp[i][j] = max(min_from_up, min_from_left)

print(dp[N-1][N-1])