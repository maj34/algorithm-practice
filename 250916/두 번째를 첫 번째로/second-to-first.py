char = list(input())

second = char[1]

for i in range(len(char)):
    if char[i] == second:
        char[i] = char[0]

print(''.join(char))