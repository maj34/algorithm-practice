numbers = []
for _ in range(10):
    numbers.append(int(input()))

num = 0
for i in numbers:
    if i%2!=0:
        num+=1

print(num)