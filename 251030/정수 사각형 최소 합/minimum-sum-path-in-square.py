N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][N-1] = grid[0][N-1]

# 첫번째 행 
for i in range(N-2, -1, -1):
    dp[0][i] = dp[0][i+1] + grid[0][i]

# 마지막 열
for j in range(1, N):
    dp[j][N-1] = dp[j-1][N-1] + grid[j][N-1]
print(dp)

# # 그 외의 값 채우기
# for k in range(N-2, -1, -1):
#     for l in range(N-2, -1, -1):
#         dp[k][l] = min(dp[k-1][l], dp[k][l+1]) + grid[k][l]

# # 출력
# print(dp)
# print(dp[N-1][0])