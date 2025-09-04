N, B = map(int, input().split())

def notation(N, B):
    digits = []
    while True:
        if N <= 1:
            digits.append(N)
            break
        digits.append(N%B)
        N //= B
    for i in digits[::-1]:
        print(i, end="")

notation(N, B)