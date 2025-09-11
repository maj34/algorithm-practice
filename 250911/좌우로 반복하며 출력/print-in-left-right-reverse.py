N = int(input())

for i in range(N):
    for j in range(1, N+1):
        if i%2==0:
            print(j, end="")
        else:
            print(N-j+1, end="")
    print()