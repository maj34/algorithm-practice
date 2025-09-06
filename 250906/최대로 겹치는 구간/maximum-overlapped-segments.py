n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

max_num = 0
for i in segments:
    for j in [0, 1]:
        if i[j] > max_num:
            max_num = i[j]

blocks = [0]*(max_num+1)

for i in segments:
    for j in range(i[0], i[1]+1):
        blocks[j] += 1

print(max(blocks))