N, B = map(int, input().split())

def notation(N, B):
    digits = []
    while N > 0:
        digits.append(N % B)
        N //= B
    for i in digits[::-1]:
        print(i, end="")

notation(N, B)