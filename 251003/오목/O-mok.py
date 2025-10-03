board = [list(map(int, input().split())) for _ in range(19)]

movement = [[0, 1], [1, -1], [-1, 1], [1, 1], [-1, -1], [0, -1], [1, 0], [-1, 0]]

# black: 1, white: 2
found_winner = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] != 0:
            # 바둑돌 진입
            winner = board[i][j]
            for idx, m in enumerate(movement):
                winner_arr = [[i, j]]
                if 0 <= i + m[0] < len(board) or 0 <= j + m[1] < len(board[0]):
                    if board[i + m[0]][j + m[1]] == winner: # 두 번째 돌도 맞음
                        winner_arr.append([i + m[0], j + m[1]])
                        # print("winner_arr", winner_arr)
                        for k in range(2, 5):
                            if 0 <= i + m[0] < len(board) or 0 <= j + m[1] < len(board[0]):
                                if board[i + (m[0] * k)][j + (m[1] * k)] == winner:
                                    winner_arr.append([i + (m[0] * k), j + (m[1] * k)])
                                else:
                                    break
                            else:
                                break
                        if len(winner_arr) == 5:
                            # print("winner_arr:", winner_arr)
                            print(winner)
                            print(winner_arr[2][0] + 1, winner_arr[2][1] + 1)
                            # exit(0)
                    else:
                        break
                else:
                    break
        

