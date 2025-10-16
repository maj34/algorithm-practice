from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

visited = [[False] * n for _ in range(n)]
q = deque()

def bfs(si, sj):
    q.append((si, sj))
    visited[si][sj] = True
    while q:
        ci, cj = q.popleft()
        
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            # 갈 수 있는 곳인지 판단
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and grid[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = True
    
for k in points:
    bfs(k[0]-1, k[1]-1)
        
print((sum(visited[i][j]==True for i in range(n) for j in range(n))))