n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y]==1

def dfs(x, y):
    cnt = 1
    visited[x][y] = True

    # 상하좌우 탐색
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        if can_go(nx, ny):
            cnt += dfs(nx, ny)
    return cnt

villages = []

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            count = dfs(i, j)
            villages.append(count)

print(len(villages))
for i in sorted(villages):
    print(i)