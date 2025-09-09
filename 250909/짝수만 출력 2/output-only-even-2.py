B, A = map(int, input().split())

while A <= B:
    if B%2==0:
        print(B, end=" ")
    B -= 1