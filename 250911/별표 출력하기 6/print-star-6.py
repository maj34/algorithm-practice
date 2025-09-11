N = int(input())

tmp = 0
for i in range(2*N-1, 1, -2):
    print("  "*tmp, end="")
    print("* "*i)
    tmp += 1

for j in range(1, 2*N, 2):
    print("  "*tmp, end="")
    print("* "*j)
    tmp -= 1