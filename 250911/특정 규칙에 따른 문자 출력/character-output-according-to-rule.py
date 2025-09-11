N = int(input())

tmp = N-1
for i in range(1, N):
    print("  "*tmp, end="")
    print("@ "*i)
    tmp -= 1

for j in range(N, 0, -1):
    print("@ "*j)