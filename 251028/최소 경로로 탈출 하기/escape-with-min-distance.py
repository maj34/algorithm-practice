from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(si, sj, arr):
    q = deque()
    visited = [[False]*m for i in range(n)]

    q.append((si, sj))
    visited[si][sj] = True

    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0<= ni < n and 0<= nj < m and not visited[ni][nj] and arr[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = True
                arr[ni][nj] = arr[ci][cj] + 1
    # 종료조건
    if arr[n-1][m-1] > 1:
        print(arr[n-1][m-1]-1)
    else:
        print(-1)
    
bfs(0, 0, arr)