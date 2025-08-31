a, b = map(int, input().split())

import math

def is_prime(n):
    if n == 1 :
        return False
    if n == 2:
        return True 
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_even(n):
    ssum = 0
    for i in str(n):
        ssum += int(i)
    return ssum % 2 == 0

num = 0
for i in range(a, b+1):
    if is_prime(i) and is_even(i):
        num += 1

print(num)