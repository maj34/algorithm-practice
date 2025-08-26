s = list(input())

s[1] = "a"
s[-2] = "a"

for i in s:
    print(i, end="")