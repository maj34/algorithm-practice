char = input()

for i in char:
    if 65 <= ord(i) <= 90:
        print(i.lower(), end="")
    elif 97 <= ord(i) <= 122:
        print(i.upper(), end="")