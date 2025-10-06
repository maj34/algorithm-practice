n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
is_consecutive = 0

# 행 기준 연속적인 숫자 판단
for row in grid:
    cnt = 1
    for i in range(n-1):
        if row[i] == row[i+1]:
            cnt += 1
        if cnt >= m:
            is_consecutive += 1
            break
            
# 열 기준 연속적인 숫자 판단
col_val = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        col_val[i].append(grid[j][i])

for col in col_val:
    cnt = 1
    for i in range(n-1):
        if col[i] == col[i+1]:
            cnt += 1
        if cnt >= m:
            is_consecutive += 1
            break

print(is_consecutive)