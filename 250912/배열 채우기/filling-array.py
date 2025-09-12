arr = map(int, input().split())

reversed_arr = []
for i in arr:
    if i==0:
        break
    else:
        reversed_arr.append(i)

print(*reversed_arr[::-1])