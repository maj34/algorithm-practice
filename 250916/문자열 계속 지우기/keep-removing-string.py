string = list(input())
char = list(input())

while True:
    found = False
    for i in range(len(string)-len(char)+1):
        if string[i:i+len(char)] == char:
            string = string[:i] + string[i+len(char):]
            found=True
            break
    if not found:
        break

print("".join(string))