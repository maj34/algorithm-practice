n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

num = []
for i in range(n):
    for j in range(n-2):
        num.append(grid[i][j] + grid[i][j+1] + grid[i][j+2])

print(max(num))