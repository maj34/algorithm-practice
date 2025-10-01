R, C = map(int, input().split())
square = [list(input().split()) for _ in range(R)]

# cnt = []
# for i in range(R):
#     for j in range(C):
#         for k in range(i+1, R-1):
#             for l in range(j+1, C-1):
#                 if grid[i][j] != grid[k][l]:
#                     for a in range(k+1, R-1):
#                         for b in range(l+1, C-1):
#                             if grid[k][l] != grid[a][b]:
#                                 cnt.append(str(k)+str(l)+str(a)+str(b))

# print(len(set(cnt)))

# 시작점과 도착점의 색상
# start_color = grid[0][0]
# end_color = grid[R-1][C-1]

# count = 0

# # 첫 번째 점프 지점 (r1, c1) 찾기
# for r1 in range(1, R):
#     for c1 in range(1, C):
        
#         # 두 번째 점프 지점 (r2, c2) 찾기
#         # (r1, c1) 보다 반드시 크고, 도착점보다는 작아야 함
#         for r2 in range(r1 + 1, R - 1):
#             for c2 in range(c1 + 1, C - 1):
                
#                 # 점프 지점들의 색상
#                 jump1_color = grid[r1][c1]
#                 jump2_color = grid[r2][c2]
                
#                 # 3가지 색상 변경 조건을 모두 만족하는지 확인
#                 if start_color != jump1_color and \
#                    jump1_color != jump2_color and \
#                    jump2_color != end_color:
#                     count += 1

# print(count)


start = square[0][0]
end = square[R - 1][C - 1]
if start == end:
    print(0)
    exit(0)

answer = 0
for i, sq in enumerate(square):
    for j, s in enumerate(sq):
        if (i == 0 and j == 0) or (i == R - 1 and j == C - 1):
            continue
        # print("s:", s)
        if s == end:
            # print("s == end")
            # print("square[i + 1:R - 1]:", square[i + 1:R - 1])
            for k in square[i + 1:R - 1]:
                # print("k:", k, "i:", i, "j:", j)
                for m in k[j + 1:C - 1]:
                    # print("m:", m)
                    if m != end:
                        answer += 1

print(answer)