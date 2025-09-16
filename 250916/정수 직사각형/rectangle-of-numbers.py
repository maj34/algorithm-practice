N, M = map(int, input().split())

num = 1
for _ in range(N):
    for _ in range(M):
        print(num, end=" ")
        num += 1
    print()