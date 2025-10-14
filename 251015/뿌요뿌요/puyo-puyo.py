n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def can_go(x, y, num):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == num

def dfs(x, y, num):
    cnt = 1
    visited[x][y] = True

    # 상하좌우 방향
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, num):        
            cnt += dfs(nx, ny, num)
    return cnt

max_num = max(max(n) for n in grid)

num_cnt = {}
for num in range(1, max_num+1):
    for i in range(n):
        for j in range(n):
            if can_go(i, j, num):
                count = dfs(i, j, num)
                if num in num_cnt:
                    num_cnt[num].append(count)
                else:
                    num_cnt[num] = [count]

over_num, max_sum = 0, 0
for k, v in num_cnt.items():
    if max(v) >= 4:
        over_num += 1
    max_sum = max(max_sum, max(v))

print(over_num, max_sum)