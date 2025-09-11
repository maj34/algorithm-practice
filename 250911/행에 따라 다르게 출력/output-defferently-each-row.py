N = int(input())

num = 0
for i in range(N):
    for j in range(N):
        if i%2==0:
            num += 1
            print(num, end=" ")
        else:
            num += 2
            print(num, end=" ")
    print()
