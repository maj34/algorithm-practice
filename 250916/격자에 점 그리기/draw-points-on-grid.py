N, M = map(int, input().split())

arr = [
    [0] * N
    for _ in range(N)
]

num = 1
for _ in range(M):
    r, c = map(int, input().split())
    arr[r-1][c-1] = num
    num += 1

for i in arr:
    for j in i:
        print(j, end=" ")
    print()