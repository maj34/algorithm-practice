from itertools import combinations

# 입력 받기
N, M, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 특정 구간(연속 M개)에서 훔칠 수 있는 최대 가치 계산
def get_best_value(row, start_col):
    items = grid[row][start_col:start_col + M]
    best = 0
    # 모든 부분집합 탐색 (공집합 제외)
    for r in range(1, M + 1):
        for comb in combinations(items, r):
            if sum(comb) <= C:
                best = max(best, sum(x * x for x in comb))
    return best

# 모든 가능한 선택 경우를 저장
choices = []
for r in range(N):
    for c in range(N - M + 1):
        choices.append((r, c, get_best_value(r, c)))

# 두 도둑이 훔칠 수 있는 최대 가치 계산
ans = 0
for i in range(len(choices)):
    r1, c1, v1 = choices[i]
    for j in range(i + 1, len(choices)):
        r2, c2, v2 = choices[j]
        # 같은 행이면 겹치지 않아야 함
        if r1 == r2 and not (c1 + M <= c2 or c2 + M <= c1):
            continue
        ans = max(ans, v1 + v2)

print(ans)