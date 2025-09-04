n = int(input())

# print(format(n, 'b'))
# print(bin(n)[2:])

digits = []
while True:
    if n <= 1:
        digits.append(n)
        break
    digits.append(n%2)
    n //= 2

for i in digits[::-1]:
    print(i, end="")