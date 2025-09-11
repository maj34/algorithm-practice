N = int(input())

num = 1
for _ in range(N):
    for _ in range(N):
        print(num, end=" ")
        num += 1
    print()