N, M = map(int, input().split())
arr = [input() for _ in range(N)]

movements = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
# Please write your code here.
cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L': # L 시작
            # 두 번째 체크
            for mov in movements:
                if 0 <= i + mov[0] < N and 0 <= j + mov[1] < M:
                    if arr[i + mov[0]][j + mov[1]] == 'E': # 두 번째 맞음
                        # print(f"LE at: {i} {j}, {i + mov[0]} {j + mov[1]}")
                        if 0 <= i + mov[0] * 2 < N and 0 <= j + mov[1] * 2 < M:
                            if arr[i + mov[0] * 2][j + mov[1] * 2] == 'E': # 세 번째 맞음
                                cnt += 1

print(cnt)

