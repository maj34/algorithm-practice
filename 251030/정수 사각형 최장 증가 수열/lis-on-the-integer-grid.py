from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

def bfs(si, sj):
    q = deque()
    visited = [[False]* N for _ in range(N)]

    q.append((si, sj, 1))
    visited[si][sj] = True

    while q:
        ci, cj, cnt = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and grid[ni][nj] > grid[ci][cj]:
                q.append((ni, nj, cnt+1))
                visited[ni][nj] = True
    
    return cnt

max_cnt = 0
for i in range(N):
    for j in range(N):
        cnt = bfs(i, j)
        max_cnt = max(max_cnt, cnt)

print(max_cnt)