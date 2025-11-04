N = int(input())
x1, x2 = [], []
for _ in range(N):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

segments = []
for i in range(N):
    segments.append((x1[i], x2[i]))

segments.sort(key=lambda x: x[1])

count = 0
last_end_time = 0

for start, end in segments:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)