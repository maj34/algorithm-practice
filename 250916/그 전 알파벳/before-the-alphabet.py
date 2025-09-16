char = input()

if ord(char)==97:
    print(chr(ord(char)+26-1))
else:
    print(chr(ord(char)-1))