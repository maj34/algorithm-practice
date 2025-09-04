binary = input()

# print(int(binary, 2))

num = 0
for i in range(len(binary)):
    num += int(binary[-1-i]) * 2**i

print(num)