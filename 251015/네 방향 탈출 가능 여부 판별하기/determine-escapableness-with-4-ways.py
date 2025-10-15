from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        if x==n-1 and y==m-1:
            print(1)
            return

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                
    print(0)

bfs()