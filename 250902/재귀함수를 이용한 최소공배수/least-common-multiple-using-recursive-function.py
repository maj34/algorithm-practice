n = int(input())
arr = list(map(int, input().split()))

from math import lcm

def recursive(i, acc):
    if i == n:
        return acc
    return recursive(i+1, lcm(acc, arr[i]))

print(recursive(1, arr[0]))
