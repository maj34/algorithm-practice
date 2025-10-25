from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 외부 물(0) 영역을 탐색
def bfs_air():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if a[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif a[nx][ny] == 1:
                    # 외부 공기와 닿아 있는 빙하를 2로 표시
                    a[nx][ny] = 2
    return visited

# 2로 표시된 빙하를 녹이고 0으로 변경
def melt():
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2:
                a[i][j] = 0

# 현재 빙하의 개수
def count_ice():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                cnt += 1
    return cnt

time = 0
last = 0

while True:
    ice = count_ice()
    if ice == 0:
        print(time, last)
        break
    last = ice
    bfs_air()
    melt()
    time += 1