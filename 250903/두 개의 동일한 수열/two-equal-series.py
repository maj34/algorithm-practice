n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sorted(A) == sorted(B):
    print("Yes")
else:
    print("No")