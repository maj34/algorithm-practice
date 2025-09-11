N = int(input())

for i in range(1, N+1):
    for j in range(1, N+1):
        if j > i:
            break
        print(j, end=" ")
    print()