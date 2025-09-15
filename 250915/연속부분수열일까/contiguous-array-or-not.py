A, B = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

# if arr_b[0] in arr_a:
#     idx = arr_a.index(arr_b[0])
#     for i in range(len(arr_b)):
#         if arr_b[i] == arr_a[idx+i]:
#             is_true=True
#         else:
#             is_true=False
#             break
# else:
#     is_true=False

# print("Yes") if is_true else print("No")

str_a = " ".join(map(str, arr_a))
str_b = " ".join(map(str, arr_b))

print("Yes") if str_b in str_a else print("No")