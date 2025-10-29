N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

# 시작값
dp[0][0] = grid[0][0]

# 첫번째 행, 열 채우기
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + grid[i][0] # 첫번째 열
    dp[0][i] = dp[0][i-1] + grid[0][i] # 첫번째 행

# 그 외의 값 채우기
for k in range(1, N):
    for l in range(1, N):
        dp[k][l] = max(dp[k-1][l], dp[k][l-1]) + grid[k][l]

# 출력
print(dp[N-1][N-1])