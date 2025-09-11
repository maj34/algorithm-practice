N = int(input())

tmp = N-1
for i in range(1, N):
    print(" "*tmp, end="")
    print("* "*i)
    tmp -= 1

tmp = 0
for j in range(N, 0, -1):
    print(" "*tmp, end="")
    print("* "*j)
    tmp += 1