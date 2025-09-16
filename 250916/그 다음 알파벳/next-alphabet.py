char = input()

if ord(char)==122:
    print(chr(ord(char)-26+1))
else:
    print(chr(ord(char)+1))