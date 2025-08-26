s = input()

fruits = ["apple", "banana", "grape", "blueberry", "orange"]
num = 0
same = []

for i in fruits:
    if i[1] == s or i[2] == s:
        num += 1
        same.append(i)
    else:
        continue

for j in same:
    print(j)
print(num)