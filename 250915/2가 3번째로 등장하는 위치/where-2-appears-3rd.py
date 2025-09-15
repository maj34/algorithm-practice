N = int(input())
arr = list(map(int, input().split()))

for _ in range(2):
    arr.pop(arr.index(2))
    
print(arr.index(2)+3)