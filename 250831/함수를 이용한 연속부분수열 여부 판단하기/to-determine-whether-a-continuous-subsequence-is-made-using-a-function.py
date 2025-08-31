n1, n2 = map(int, input().split())
a = list(map(str, input().split()))
b = list(map(str, input().split()))

# def continuous_subarray(a, b):
#     for i in range(n1 - n2 + 1):
#         if a[i:i+n2] == b:
#             return "Yes"
#     return "No"

# print(continuous_subarray(a, b))

def continuous_subarray(a, b):
    a_tmp = ' '.join(a)
    b_tmp = ' '.join(b)

    if b_tmp in a_tmp:
        return "Yes"
    return "No"

print(continuous_subarray(a, b))