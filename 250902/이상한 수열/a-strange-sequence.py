N = int(input())

def recursive(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    return recursive(N//3) + recursive(N-1)

print(recursive(N))