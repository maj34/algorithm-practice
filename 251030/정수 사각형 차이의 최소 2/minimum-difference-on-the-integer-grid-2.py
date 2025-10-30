from collections import deque
import sys

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

min_diff = sys.maxsize

q = deque()
q.append((0, 0, [grid[0][0]]))  # 현재까지 경로에 포함된 값들의 list까지 저장

while q:
    ci, cj, current_path_values = q.popleft()

    # 목적지에 도달한 경우
    if ci == N - 1 and cj == N - 1:
        current_max = max(current_path_values)
        current_min = min(current_path_values)
        diff = current_max - current_min
        
        min_diff = min(min_diff, diff)
        continue 
        
    for di, dj in [(1, 0), (0, 1)]:
        ni, nj = ci + di, cj + dj
        
        if 0 <= ni < N and 0 <= nj < N:
            # current_path_values 리스트를 복사하고 새 값을 추가
            new_path_values = list(current_path_values)
            new_path_values.append(grid[ni][nj])
            
            q.append((ni, nj, new_path_values))

print(min_diff)