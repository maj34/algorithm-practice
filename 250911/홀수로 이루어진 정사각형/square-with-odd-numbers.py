N = int(input())

num = 11
for i in range(N):
    for j in range(N):
        print(num, end=" ")
        num += 2
    num = num - 2*(N-1)
    print()