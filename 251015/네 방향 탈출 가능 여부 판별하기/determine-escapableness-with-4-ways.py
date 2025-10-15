from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1

def bfs():
    # q에 남은 것이 없을 때까지 반복
    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

# 시작점을 q에 넣고 시작
q.append((0, 0))
visited[0][0] = True

bfs()

# 우측 하단을 방문한 적이 있는지 여부 출력
print(1 if visited[n-1][m-1] else 0)    