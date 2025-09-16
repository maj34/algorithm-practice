N = int(input())

num=1
for i in range(N):
    for j in range(N):
        print(num, end=" ")
        num+=N
    num-=(N*N-1)
    print()