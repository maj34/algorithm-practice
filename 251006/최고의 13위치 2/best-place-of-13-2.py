n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                if i == k and j == l:
                    continue
                elif i == k and j+1 == l:
                    continue
                elif i == k and j+2 == l:
                    continue
                else:
                    arr_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                            arr[k][l] + arr[k][l+1] + arr[k][l+2]
                    max_sum = max(max_sum, arr_sum)

print(max_sum)