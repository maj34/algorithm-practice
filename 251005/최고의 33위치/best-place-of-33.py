n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for i in range(n-2):
    for j in range(n-2):
        ssum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
        max_sum = max(max_sum, ssum)

print(max_sum)