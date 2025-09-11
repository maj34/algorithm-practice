N = int(input())

tmp = N-1
for i in range(1, 2*N-1, 2):
    print(" "*tmp, end="")
    print("*"*i)
    tmp -= 1

tmp = 0
for j in range(2*N-1, 0, -2):
    print(" "*tmp, end="")
    print("*"*j)
    tmp += 1