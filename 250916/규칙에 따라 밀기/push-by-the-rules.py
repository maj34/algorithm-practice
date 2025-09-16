char = input()
command = list(input())

for i in command:
    if i == "L":
        char = char[1:] + char[:1]
    elif i == "R":
        char = char[-1:] + char[:-1]

print(char)