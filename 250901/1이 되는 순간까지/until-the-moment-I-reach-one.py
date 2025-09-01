N = int(input())

def recursive(N):
    if N == 1:
        return 0
    if N % 2 == 0:
        return recursive(N//2) + 1
    else:
        return recursive(N//3) + 1
    
print(recursive(N))