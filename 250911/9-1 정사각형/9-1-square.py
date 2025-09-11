N = int(input())

num = 9
for _ in range(N):
    for j in range(N):
        if num%10==0:
            num -= 1
        print(num%10, end="")
        num -= 1
    print()