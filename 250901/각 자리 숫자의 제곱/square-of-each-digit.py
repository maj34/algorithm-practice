N = int(input())

def recursive(N):
    if N < 10:
        return N**2
    return recursive(N//10) + (N%10)**2

print(recursive(N))