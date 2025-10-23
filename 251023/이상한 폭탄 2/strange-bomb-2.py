N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

positions = {}

for i in range(N):
    bomb_num = num[i]
    if bomb_num not in positions:
        positions[bomb_num] = []
    positions[bomb_num].append(i)

max_bomb = -1

for bomb_num, indices in positions.items():
    if len(indices) < 2:
        continue
        
    for i in range(len(indices) - 1):
        dist = indices[i+1] - indices[i]
        
        if dist <= K:
            max_bomb = max(max_bomb, bomb_num)
            break

print(max_bomb)