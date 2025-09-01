n = int(input())

def recursive(n):
    if n == 0:
        return        
    recursive(n-1)
    print(n, end=" ")

def reverse_recursive(n):
    if n == 0:
        return
    print(n, end=" ")        
    reverse_recursive(n-1)
    
recursive(n)
print()
reverse_recursive(n)
    