from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
grid = [list(map(int, input().split())) for _ in range(N)]

# 격자 전체의 최솟값, 최댓값
min_val = min(map(min, grid))
max_val = max(map(max, grid))

# 오른쪽, 아래로만 이동해서 N-1, N-1까지 도달 가능한지 검사
def can_reach(diff, start_min):
    start_max = start_min + diff
    # 시작 칸이 구간 안에 있지 않으면 바로 불가능
    if not (start_min <= grid[0][0] <= start_max):
        return False

    q = deque([(0, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True

    while q:
        i, j = q.popleft()
        if i == N - 1 and j == N - 1:
            return True

        for di, dj in [(1, 0), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if start_min <= grid[ni][nj] <= start_max:
                    visited[ni][nj] = True
                    q.append((ni, nj))
    return False

# 이분 탐색으로 최소 차이 찾기
left, right = 0, max_val - min_val
answer = right

while left <= right:
    mid = (left + right) // 2
    possible = False

    # start_min을 가능한 값들로 옮겨가며 검사
    for start_min in range(min_val, max_val - mid + 1):
        if can_reach(mid, start_min):
            possible = True
            break

    if possible:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)