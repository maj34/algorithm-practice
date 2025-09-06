n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

blocks = [0]*n

for i in commands:
    for j in range(i[0]-1, i[1]):
        blocks[j] += 1

print(max(blocks))