N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

for j in numbers:
    if j%2!=0 and j%3==0:
        print(j)
    else:
        continue