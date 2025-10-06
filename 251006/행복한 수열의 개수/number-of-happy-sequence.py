n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def consecutive_cnt(array):
    max_res = 0
    answer = 0
    start = None
    for arr in array:
        if arr == start: # consecutive
            start = arr
            answer += 1
        else: # not consecutive
            start = arr
            if answer > max_res:
                max_res = answer
            answer = 1
    if answer > max_res:
        max_res = answer
    return max_res
    
ans = 0
for g in grid:
    if consecutive_cnt(g) >= m:
        ans += 1

rev_arr = [[] for _ in range(len(grid))]
for i in range(len(grid[0])):
    for j in range(len(grid)):
        rev_arr[i].append(grid[j][i])

for g in rev_arr:
    if consecutive_cnt(g) >= m:
        ans += 1

print(ans)