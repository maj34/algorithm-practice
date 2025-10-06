n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for i in range(n-1):
    for j in range(n-2):
        arr_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
        max_sum = max(max_sum, arr_sum)

print(max_sum)