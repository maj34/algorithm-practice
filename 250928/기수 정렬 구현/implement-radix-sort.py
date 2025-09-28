n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def radix_sort(arr, k):
    for pos in range(k):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // (10 ** pos)) % 10
            buckets[digit].append(num)
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
    return arr

# 예시 실행
result = radix_sort(arr, len(str(max(arr))))
print(*result)