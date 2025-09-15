A, B = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

idx = arr_a.index(arr_b[0]) if arr_b[0] in arr_a else None

for i in range(len(arr_b)):
    if arr_b[i] == arr_a[idx+i]:
        is_true=True
    else:
        is_true=False
        break

print("Yes") if is_true else print("No")