from collections import Counter
A, B = map(int, input().split())

arr = []
while True:
    arr.append(A%B)
    A = A//B
    if A <= 1:
        break

val_sum = 0
for i in Counter(arr).values():
    val_sum += i**2

print(val_sum)