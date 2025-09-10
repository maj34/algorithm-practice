N = int(input())

tmp = 0
for i in range(N, 0, -1):
    print("*"*i, end="")
    print(" "*tmp, end="")
    print("*"*i)
    tmp+=2