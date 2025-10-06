n = int(input())
lst = [i for i in range(1, n+1)]

while len(lst) != 1:
    lst = lst[2:] + [lst[1]]

print(*lst)