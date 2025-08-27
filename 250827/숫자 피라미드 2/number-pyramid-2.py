N = int(input())

num = 1
row = 1
for i in range(N):
    for j in range(row):
        print(num, end=" ")
        num += 1
    print()
    row += 1