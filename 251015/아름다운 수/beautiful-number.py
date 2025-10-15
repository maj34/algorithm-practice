from itertools import product

def is_beautiful(num):
    i = 0
    n = len(num)
    while i < n:
        digit = int(num[i])
        # digit 만큼 반복되는지 검사
        if i + digit > n:  # 길이 초과
            return False
        # digit 길이만큼 동일한 숫자가 있는지 검사
        for j in range(i, i + digit):
            if int(num[j]) != digit:
                return False
        i += digit  # 다음 그룹으로 이동
    return True

N = int(input())
count = 0

# 1~4로 이루어진 모든 N자리 수 생성
for comb in product("1234", repeat=N):
    num = ''.join(comb)
    if is_beautiful(num):
        count += 1

print(count)