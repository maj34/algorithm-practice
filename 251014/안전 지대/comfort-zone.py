n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def can_go(x, y, h, visited):
    return in_range(x, y) and not visited[x][y] and grid[x][y]>h

def dfs(x, y, h, visited):
    visited[x][y] = True
    # 상하좌우 탐색
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        if can_go(nx, ny, h, visited):
            dfs(nx, ny, h, visited)

area = {}
max_height = max(max(grid))

for k in range(1, max_height+1):
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k, visited):
                dfs(i, j, k, visited)
                count += 1
    area[k] = count

sorted_area = sorted(area.items(), key=lambda x: x[1], reverse=True)
print(*sorted_area[0])