n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_sum = []
for i in range(n):
    for j in range(n-2):
        arr_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        max_sum.append(arr_sum)

max_sum.sort(reverse=True)
print(max_sum[0] + max_sum[1])