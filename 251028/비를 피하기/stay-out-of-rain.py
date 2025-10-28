from collections import deque

N, H, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(si, sj):
    q = deque()
    visited = [[False]*N for i in range(N)]

    q.append((si, sj, 0))
    visited[si][sj] = True

    dist = 0
    while q:
        ci, cj, dist = q.popleft()
        
        # 종료조건
        if arr[ci][cj] == 3:
            return dist

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] != 1:
                q.append((ni, nj, dist+1))
                visited[ni][nj] = True
            
    return -1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            print(bfs(i, j), end=" ")
        else: 
            print(0, end=" ")
    print()