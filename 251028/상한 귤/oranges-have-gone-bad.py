from collections import deque

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    q = deque()
    visited = [[False] * N for _ in range(N)]

    # 상한 귤을 시작점으로 상하는 시간 계산
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                q.append((i, j))
                visited[i][j] = True

    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] == 1:
                arr[ni][nj] = arr[ci][cj] + 1
                q.append((ni, nj))
                visited[ni][nj] = True

bfs()

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            print(-1, end=" ")
        elif arr[i][j] == 1:
            print(-2, end=" ")
        else:
            print(arr[i][j]-2, end=" ")
    print()