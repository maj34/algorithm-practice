N = int(input())
sequence = list(map(int, input().split()))

dp_lis = [1] * N
for i in range(1, N):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp_lis[i] = max(dp_lis[i], dp_lis[j] + 1)

dp_lds = [1] * N
for i in range(N - 2, -1, -1):
    for j in range(N - 1, i, -1):
        if sequence[i] > sequence[j]:
            dp_lds[i] = max(dp_lds[i], dp_lds[j] + 1)

max_len = 0
for i in range(N):
    max_len = max(max_len, dp_lis[i] + dp_lds[i] - 1)

print(max_len)