n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def consecutive(array):
    is_consecutive = 0
    if len(array) == 1:
        cnt = 1
        if cnt >= m:
            return 1
    
    for arr in array:
        prev_num = arr[0]
        cnt = 1
        for i in range(n-1):
            if prev_num == arr[i] == arr[i+1]:
                cnt += 1
            else:
                cnt = 1
                prev_num = arr[i+1]

            if cnt >= m:
                is_consecutive += 1
                break
    return is_consecutive
            
col_val = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        col_val[i].append(grid[j][i])

print(consecutive(grid)+consecutive(col_val))