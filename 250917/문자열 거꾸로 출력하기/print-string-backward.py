for _ in range(10):
    char = input()
    if char == "END":
        break
    for i in list(char)[::-1]:
        print(i, end="")
    print()
