a, b = map(int, input().split())
n = input()

def notation(n, b):
    digits = []
    while n > 0:
        digits.append(n % b)
        n //= b
    for i in digits[::-1]:
        print(i, end="")

notation(int(n, a), b)