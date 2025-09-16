string = input()
arr = list(string)

arr[1] = "a"
arr[-2] = "a"

for i in arr:
    print(i, end="")