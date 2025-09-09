A, B = map(int, input().split())

integer_part = A // B
result = str(integer_part) + "."

A %= B
for _ in range(20):  
    A *= 10
    digit = A // B   
    result += str(digit)
    A %= B

print(result)