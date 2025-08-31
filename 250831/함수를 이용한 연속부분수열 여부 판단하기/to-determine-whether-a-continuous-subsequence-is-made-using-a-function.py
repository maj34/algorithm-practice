n1, n2 = map(int, input().split())
a = input().replace(" ", "")
b = input().replace(" ", "")

def continuous_subarray(a, b):
    if str(b) in str(a):
        return "Yes"
    return "No"

print(continuous_subarray(a, b))