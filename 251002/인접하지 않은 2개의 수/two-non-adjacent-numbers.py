n = int(input())
numbers = list(map(int, input().split()))

max_num = 0
# 인덱스 i
for i in range(n-2):
    # 더해지는 값 j
    for j in range(2, n-i):
        num = numbers[i] + numbers[i+j]
        max_num = max(max_num, num)

print(max_num)