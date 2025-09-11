N = int(input())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

for j in range(1, N+1):
    if is_prime(j):
        print(j, end=" ")