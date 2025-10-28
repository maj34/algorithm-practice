from collections import deque
from itertools import combinations

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

def bfs(si, sj, arr):
    q = deque()
    visited = [[False] * N for _ in range(N)]

    q.append((si, sj, 0))
    visited[si][sj] = True

    while q:
        ci, cj, dist = q.popleft()

        if ci == (r2-1) and cj == (c2-1):
            return dist
        
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] == 0:
                q.append((ni, nj, dist+1))
                visited[ni][nj] = True
            
    return 10000

lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            lst.append((i, j))

min_dist = 10000
for comb in combinations(lst, K):
    for (i, j) in comb:
        arr[i][j] = 0
    dist = bfs(r1-1, c1-1, arr)
    min_dist = min(min_dist, dist)
    for (i, j) in comb:
        arr[i][j] = 1

print(-1 if min_dist == 10000 else min_dist) 