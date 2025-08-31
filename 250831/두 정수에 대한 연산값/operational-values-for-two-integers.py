a, b = map(int, input().split())

def solution(a, b):
    if a > b:
        a += 25
        b *= 2
        return a, b
    else:
        b += 25
        a *= 2
        return a, b

a, b = solution(a, b)
print(a, b)