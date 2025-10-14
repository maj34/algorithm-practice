n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 0:
        return False
    return True

answer = False

def dfs(x, y):
    global answer

    if x == n-1 and y == m-1:
        answer = True
        return

    visited[x][y] = True

    # 오른쪽, 아래쪽으로만 이동
    for dx, dy in [(0, 1), (1, 0)]:
        new_x, new_y = x+dx, y+dy

        if can_go(new_x, new_y):
            dfs(new_x, new_y)

dfs(0, 0)
print(1 if answer else 0)