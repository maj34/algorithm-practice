char = list(input())

first = char[0]
second = char[1]

for i in range(len(char)):
    if char[i] == first:
        char[i] = second
    elif char[i] == second:
        char[i] = first

print(''.join(char))