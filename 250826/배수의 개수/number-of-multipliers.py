a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())

num_list = [a, b, c, d, e, f, g, h, i, j]
three = 0
five = 0

for i in num_list:
    if i % 3 == 0:
        three += 1
        if i % 15 == 0:
            five += 1
    elif i % 5 == 0:
        five += 1
    else:
        continue

print(three, five)