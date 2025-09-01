N = int(input())

def ssum(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    return ssum(N-2) + N

print(ssum(N))