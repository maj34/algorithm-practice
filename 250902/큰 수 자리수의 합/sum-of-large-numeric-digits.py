a, b, c = map(int, input().split())

def recursive(n):
    if n < 10:
        return n
    return recursive(n // 10) + (n % 10)

print(recursive(a*b*c))