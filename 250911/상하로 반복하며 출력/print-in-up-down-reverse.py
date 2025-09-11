N = int(input())

for i in range(1, N+1):
    for j in range(N):
        print(i if j%2==0 else N-i+1, end="")
    print()