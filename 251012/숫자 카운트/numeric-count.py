from itertools import permutations

# 입력 받기
N = int(input())
queries = []
for _ in range(N):
    num, s, b = input().split()
    queries.append((num, int(s), int(b)))

# 가능한 후보 수 초기화
candidates = permutations('123456789', 3)
count = 0

# 모든 후보 검사
for cand in candidates:
    cand = ''.join(cand)
    valid = True
    for num, s, b in queries:
        strike = sum(cand[i] == num[i] for i in range(3))
        ball = sum(c in num for c in cand) - strike
        if strike != s or ball != b:
            valid = False
            break
    if valid:
        count += 1

print(count)