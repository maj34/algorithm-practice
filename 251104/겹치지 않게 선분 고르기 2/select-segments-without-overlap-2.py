N = int(input())
x1, x2 = [], []
for _ in range(N):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

segments = list(zip(x1, x2))
segments.sort(key=lambda x: x[1])

count = 0
end_time = -float('inf')

for start, end in segments:
    if start > end_time: 
        count += 1
        end_time = end

print(count)