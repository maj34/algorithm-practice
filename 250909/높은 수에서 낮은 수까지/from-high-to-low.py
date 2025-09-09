A, B = map(int, input().split())

if A<B:
    for i in range(B, A-1, -1):
        print(i, end=" ")
else:
    for i in range(A, B-1, -1):
        print(i, end=" ")