n = int(input())

def recursive(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return recursive(n//2) + 1
    else: 
        return recursive(n*3+1) + 1
    
print(recursive(n))