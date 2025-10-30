from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 격자 내 최솟값과 최댓값
min_val = min(map(min, grid))
max_val = max(map(max, grid))

# BFS로 도달 가능한지 확인
def can_reach(diff, start_min):
    start_max = start_min + diff
    if grid[0][0] < start_min or grid[0][0] > start_max:
        return False
    
    q = deque([(0, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    
    while q:
        i, j = q.popleft()
        if i == N - 1 and j == N - 1:
            return True
        
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if start_min <= grid[ni][nj] <= start_max:
                    visited[ni][nj] = True
                    q.append((ni, nj))
    return False

# 이분 탐색으로 최소 차이 구하기
left, right = 0, max_val - min_val
answer = right

while left <= right:
    mid = (left + right) // 2
    possible = False
    
    # 가능한 시작 최솟값 범위 탐색
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