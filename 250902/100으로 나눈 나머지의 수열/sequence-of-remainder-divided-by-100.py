N = int(input())

def recursive(N):
    if N == 1:
        return 2
    if N == 2:
        return 4
    return recursive(N-1) * recursive(N-2) % 100

print(recursive(N))