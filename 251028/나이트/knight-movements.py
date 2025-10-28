from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

def bfs(si, sj):
    q = deque()
    visited = [[False] * N for _ in range(N)]

    q.append((si, sj, 0))
    visited[si][sj] = True

    dist = 0
    while q:
        ci, cj, dist = q.popleft()
        if ci == (r2-1) and cj == (c2-1):
            return dist

        for di, dj in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                q.append((ni, nj, dist+1))
                visited[ni][nj] = True

    return -1

print(bfs(r1-1, c1-1))