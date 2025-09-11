N = int(input())

num = 1
for i in range(1, N+1):
    for j in range(1, N+1):
        if i < j:
            break
        print(num, end=" ")
        num += 1
    print()