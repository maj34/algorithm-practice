str = input()

stack = []
for i in range(len(str)):
    if str[i] == "(":
        stack.append("(")
    elif str[i] == ")":
        if len(stack) == 0:
            print("No")
            exit(0)
        else:
            stack.pop()

if len(stack) == 0:
    print("Yes")
else:
    print("No")