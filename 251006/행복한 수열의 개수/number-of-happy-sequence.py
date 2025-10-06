n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 행 기준 연속적인 숫자 판단
def consecutive(array):
    is_consecutive = 0
    if len(array) == 1:
        if 1 >= m:
            return 1
    
    for arr in array:
        cnt = 1
        for i in range(n-1):
            if arr[i] == arr[i+1]:
                cnt += 1
            if cnt >= m:
                is_consecutive += 1
                break
    return is_consecutive
            
# 열 기준 연속적인 숫자 판단
col_val = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        col_val[i].append(grid[j][i])

print(consecutive(grid) + consecutive(col_val))