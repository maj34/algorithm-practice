N = int(input())

for i in range(N, 0, -1):
    for j in range(N, 0, -1):
        print(f"({i},{j}) ", end="")
    print()