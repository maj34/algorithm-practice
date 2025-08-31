n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def continuous_subarray(a, b):
    for i in range(n1 - n2 + 1):
        if a[i:i+n2] == b:
            return "Yes"
    return "No"

print(continuous_subarray(a, b))
