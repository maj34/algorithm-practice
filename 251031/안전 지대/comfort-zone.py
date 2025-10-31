N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def dfs(si, sj, h, visited):
    stack = []
    stack.append((si, sj))
    visited[si][sj] = True

    while stack:
        ci, cj = stack.pop()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and grid[ni][nj]>h:
                stack.append((ni, nj))
                visited[ni][nj] = True

area = {}
max_height = max(max(grid))

for h in range(1, max_height+1):
    visited = [[False] * M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if 0<=i<N and 0<=j<M and not visited[i][j] and grid[i][j]>h:
                dfs(i, j, h, visited)
                count += 1
    area[h] = count

sorted_area = sorted(area.items(), key=lambda x: x[1], reverse=True)
print(*sorted_area[0])