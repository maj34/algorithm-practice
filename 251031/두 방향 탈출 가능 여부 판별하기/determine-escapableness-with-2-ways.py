N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

answer = False

def dfs(si, sj):
    global answer
    visited[si][sj] = True

    if si == N-1 and sj == M-1:
        answer = True
        return

    for di, dj in [(0, 1), (1, 0)]:
        ni, nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and grid[ni][nj] == 1:
            dfs(ni, nj)

dfs(0, 0)
print(1 if answer else 0)