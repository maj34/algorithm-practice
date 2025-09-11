N = int(input())

for _ in range(N):
    for i in range(N, 0, -1):
        print(f"{i} ", end="")
    print()