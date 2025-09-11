N = int(input())

num = 2
for _ in range(N):
    for _ in range(N):
        if num%10==0:
            num+=2
        print(num%10, end=" ")
        num += 2
    print()