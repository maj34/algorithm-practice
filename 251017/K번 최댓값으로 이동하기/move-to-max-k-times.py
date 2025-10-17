from collections import deque

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
R, C = map(int, input().split())

def bfs(si, sj):
    q = deque()
    visitied = [[False] * N for _ in range(N)]

    q.append((si, sj))
    visitied[si][sj] = True

    max_num = -1
    max_pos = None

    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not visitied[ni][nj] and grid[ni][nj] < grid[si][sj]:
                q.append((ni, nj))
                visitied[ni][nj] = True
                
                # 시작보다 작은 수 중, 가장 큰 수와 그 위치 탐색
                num = grid[ni][nj]
                pos = (ni, nj)

                if num > max_num:
                    max_num = num
                    max_pos = pos
                elif num == max_num:
                    if pos[0] < max_pos[0] or (pos[0] == max_pos[0] and pos[1] < max_pos[1]):
                        max_pos = pos

    if max_pos is None:
        return (si, sj)
    return max_pos

i, j = R-1, C-1
for _ in range(K):
    i, j = bfs(i, j)

print(i+1, j+1)