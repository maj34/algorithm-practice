N = int(input())

def recursive(N):
    if N == 1 or N == 2:
        return 1
    return recursive(N-2) + recursive(N-1)

print(recursive(N))