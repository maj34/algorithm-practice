N = int(input())

def recursive(N):
    if N == 1:
        return 1
    return recursive(N-1) + N

print(recursive(N))