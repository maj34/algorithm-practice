from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

# 입력
N, K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
starts = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(K)]

# 돌(1) 위치 저장
stones = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 1]

# BFS 함수
def bfs(board):
    visited = [[False]*N for _ in range(N)]
    q = deque()
    for sx, sy in starts:
        if board[sx][sy] == 0 and not visited[sx][sy]:
            q.append((sx, sy))
            visited[sx][sy] = True

    count = 0
    while q:
        x, y = q.popleft()
        count += 1
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
    return count

# 모든 조합 탐색
max_area = 0
for comb in combinations(stones, M):  # M개의 돌을 치움
    new_board = [row[:] for row in grid]
    for x, y in comb:
        new_board[x][y] = 0  # 돌 치우기

    max_area = max(max_area, bfs(new_board))

print(max_area)