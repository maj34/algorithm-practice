A, B = map(int, input().split())

while A <= B:
    if A%2!=0:
        print(A, end=" ")
        A*=2
        if A > B:
            break
    else:
        print(A, end=" ")
        A+=3
        if A > B:
            break