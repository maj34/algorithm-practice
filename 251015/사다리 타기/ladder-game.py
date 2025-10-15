from itertools import combinations

N, M = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(M)]

# 사다리를 타고 내려가 최종 결과를 계산하는 함수
def simulate(selected_lines):
    # 초기 상태: 1~N
    pos = list(range(1, N+1))
    # 선택된 가로줄만 반영 (b는 높이)
    for a, b in sorted(selected_lines, key=lambda x:x[1]):
        pos[a-1], pos[a] = pos[a], pos[a-1]
    return pos

# 전체 가로줄을 사용할 때 결과
target = simulate(lines)
answer = M

# 가로줄을 부분집합으로 선택하여 같은 결과가 되는 최소 개수 탐색
for k in range(0, M+1):
    for comb in combinations(lines, k):
        if simulate(comb) == target:
            answer = k
            print(answer)
            exit()

print(answer)