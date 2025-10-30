# import sys
# from collections import deque

# N = int(input())
# grid = [list(map(int, input().split())) for _ in range(N)]

# # dp = [[-1]*N for _ in range(N)]

# def bfs(si, sj):
#     q = deque()
#     visited = [[False]*N for _ in range(N)]

#     q.append((si, sj, [grid[0][0]]))
#     visited[si][sj] = True

#     min_max_value = sys.maxsize

#     while q:
#         if ci == N-1 and cj == N-1:
#             max_value = max(path)
#             min_max_value = min(min_max_value, max_value)

#             return min_max_value

#         ci, cj, path = q.popleft()
#         for di, dj in [(1, 0), (0, 1)]:
#             ni, nj = ci+di, cj+dj
#             if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
#                 q.append((ni, nj, path+1))
#                 visited[ni][nj] = True

# print(bfs(0, 0))


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

dp[0][0] = grid[0][0]

for i in range(1, N):
    dp[0][i] = max(dp[0][i-1], grid[0][i])

for j in range(1, N):
    dp[j][0] = max(dp[j-1][0], grid[j][0])

for i in range(1, N):
    for j in range(1, N):
        max_from_up = max(dp[i-1][j], grid[i][j])        
        max_from_left = max(dp[i][j-1], grid[i][j])
        
        dp[i][j] = min(max_from_up, max_from_left)

print(dp[N-1][N-1])