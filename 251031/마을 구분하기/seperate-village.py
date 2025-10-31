N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def dfs(si, sj):
    cnt = 1
    visited[si][sj] = True

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and grid[ni][nj] == 1:
            cnt += dfs(ni, nj)
    return cnt

villages = []

for i in range(N):
    for j in range(N):
        if 0<=i<N and 0<=j<N and not visited[i][j] and grid[i][j] == 1:
            count = dfs(i, j)
            villages.append(count)

print(len(villages))
for i in sorted(villages):
    print(i)