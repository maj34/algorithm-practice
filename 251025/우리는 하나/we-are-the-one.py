from itertools import combinations
from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def bfs(starts):
    visited = [[False] * n for _ in range(n)]
    q = deque(starts)
    for x, y in starts:
        visited[x][y] = True
    cnt = len(starts)

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                diff = abs(grid[x][y] - grid[nx][ny])
                if u <= diff <= d:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt

cities = [(i, j) for i in range(n) for j in range(n)]
ans = 0

for comb in combinations(cities, k):
    ans = max(ans, bfs(comb))

print(ans)