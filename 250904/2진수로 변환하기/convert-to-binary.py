n = int(input())

# print(format(n, 'b'))
print(bin(n)[2:])

# digits = []
# while True:
#     if n < 1:
#         break
#     digits.append(n%2)
#     n //= 2

# if len(digits) == 0:
#     print(0)
# else:
#     for i in digits[::-1]:
#         print(i, end="")