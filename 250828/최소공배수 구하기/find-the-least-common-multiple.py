n, m = map(int, input().split())

# Please write your code here.
# from math import lcm
# print(lcm(n, m))

def lcm(n, m):
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            return i
print(lcm(n, m))