N = int(input())

arr = [
    i for i in range(1, N+1)
]

for i in range(N):
    if i % 2 != 0:
        for j in range(N-1, -1, -1):
            print(arr[j], end="")
    else:
        for j in range(N): 
            print(arr[j], end="")
    print()