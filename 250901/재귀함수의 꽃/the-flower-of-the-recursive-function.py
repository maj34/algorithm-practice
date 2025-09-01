N = int(input())

def recursive(N):
    if N == 0:
        return
    print(N, end=" ")
    recursive(N-1)
    print(N, end=" ")

recursive(N)