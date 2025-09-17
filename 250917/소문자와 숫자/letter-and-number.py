char = input()

for i in char:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        print(i.lower(), end="")
    elif 48 <= ord(i) <= 57:
        print(i, end="")