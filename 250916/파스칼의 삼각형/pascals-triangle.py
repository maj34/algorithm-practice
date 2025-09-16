N = int(input())
arr = [
    [1]*i
    for i in range(1, N+1)
]

for i in range(1, N):
    for j in range(1, N):
        if i > j:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in arr:
    for j in i:
        print(j, end=" ")
    print()