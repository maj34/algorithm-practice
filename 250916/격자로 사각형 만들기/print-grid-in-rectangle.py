N = int(input())

arr = [
    [1]*N
    for i in range(N)
]

for i in range(1, N):
    for j in range(1, N):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j] + arr[i][j-1]

for i in arr:
    for j in i:
        print(j, end=" ")
    print()