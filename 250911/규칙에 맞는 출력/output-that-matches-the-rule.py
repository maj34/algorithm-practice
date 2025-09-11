N = int(input())

for i in range(N, 0, -1):
    for j in range(N):
        if i+j <= N:
            print(j+i, end=" ")
    print()