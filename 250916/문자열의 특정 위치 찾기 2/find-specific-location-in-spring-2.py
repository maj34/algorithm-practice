char = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]

num = 0
for i in arr:
    if i[2] == char or i[3] == char:
        print(i)
        num += 1
print(num)