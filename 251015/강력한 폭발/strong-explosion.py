from itertools import product

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

bombs = [
    [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
    [(1, 0), (0, -1), (0, 0), (0, 1), (-1, 0)],
    [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]
]

# 폭탄을 높는 위치 저장
positions = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 1]

max_destroy = 0

# 모든 폭탄 조합 탐색
for combo in product(range(3), repeat=len(positions)):
    destroyed = set()  # 초토화된 영역 저장
    for (x, y), bomb_type in zip(positions, combo):
        for dx, dy in bombs[bomb_type]:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:
                destroyed.add((nx,ny))
    max_destroy = max(max_destroy, len(destroyed))

print(max_destroy)