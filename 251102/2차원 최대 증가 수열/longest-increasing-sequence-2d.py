N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]

def dfs(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 1  # 자기 자신 포함

    # 오른쪽 + 아래쪽으로 점프 가능한 모든 칸 탐색
    for ni in range(i + 1, N):
        for nj in range(j + 1, M):
            if arr[ni][nj] > arr[i][j]:
                dp[i][j] = max(dp[i][j], dfs(ni, nj) + 1)

    return dp[i][j]

print(dfs(0, 0))