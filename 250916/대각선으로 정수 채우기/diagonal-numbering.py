N, M = map(int, input().split())

board = [[0] * M for _ in range(N)]
num = 1

# 1. 첫 번째 행(0행)에서 시작하는 대각선들
for start_col in range(M):
    r, c = 0, start_col
    while r < N and c >= 0:
        board[r][c] = num
        num += 1
        r += 1
        c -= 1

# 2. 마지막 열(M-1열)에서 시작하는 나머지 대각선들 (0행 제외)
for start_row in range(1, N):
    r, c = start_row, M - 1
    while r < N and c >= 0:
        board[r][c] = num
        num += 1
        r += 1
        c -= 1

# 출력
for row in board:
    print(*row)