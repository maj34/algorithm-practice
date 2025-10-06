n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# print(n,m)
# print(grid)

def consecutive_cnt(array):
    answer = 0
    start = None
    for arr in array:
        if arr == start: # consecutive
            start = arr
            answer += 1
        else: # not consecutive
            start = arr
            answer = 1
    return answer
    
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

# print(rev_arr)
print(ans)