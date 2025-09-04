n = int(input())

# print(format(n, 'b'))
digits = []
while True:
    if n < 1:
        break
    digits.append(n%2)
    n //= 2

for i in digits[::-1]:
    print(i, end="")