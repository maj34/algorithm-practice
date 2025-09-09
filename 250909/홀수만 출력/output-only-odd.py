A, B = map(int, input().split())

for i in range(A, B+1):
    if i%2!=0:
        print(i, end=" ")