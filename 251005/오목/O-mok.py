board = [list(map(int, input().split())) for _ in range(19)]

def find_winner(stone):
    stones = [(r + 1, c + 1) for r in range(19) for c in range(19) if board[r][c] == stone]
    stone_set = set(stones)

    # 4가지 방향: →, ↓, ↘, ↙
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for r, c in stones:
        for dr, dc in directions:
            count = 1
            sequence = [(r, c)]
            nr, nc = r + dr, c + dc

            while (nr, nc) in stone_set:
                sequence.append((nr, nc))
                count += 1
                if count > 5:
                    break
                nr += dr
                nc += dc

            if count == 5:    
                mid = sequence[2]
                return stone, mid

    return 0, None

winner, mid_pos = find_winner(1)
if winner == 0:
    winner, mid_pos = find_winner(2)

print(winner)
print(*mid_pos)