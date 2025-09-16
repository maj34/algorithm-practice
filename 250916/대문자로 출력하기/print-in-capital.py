char = input()

for i in char:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        print(i.upper(), end="")