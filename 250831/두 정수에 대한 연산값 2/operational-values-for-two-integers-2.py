a, b = map(int, input().split())

def solution(a, b):
    if a > b:
        a *= 2
        b += 10
    else:
        b *= 2
        a += 10
    return a, b

for i in solution(a, b):
    print(i, end=" ")