from itertools import product

expr = input().strip()
letters = sorted(set([ch for ch in expr if ch.isalpha()]))

max_val = -2**31

# 알파벳에 1~4 사이 숫자를 할당하는 모든 조합 탐색
for values in product(range(1, 5), repeat=len(letters)):
    mapping = dict(zip(letters, values))
    
    # 식에서 알파벳을 해당 숫자로 치환
    replaced = ''.join(str(mapping[ch]) if ch.isalpha() else ch for ch in expr)
    
    # 모든 연산을 왼쪽부터 순차적으로 계산
    tokens = []
    num = ''
    for ch in replaced:
        if ch.isdigit():
            num += ch
        else:
            tokens.append(int(num))
            tokens.append(ch)
            num = ''
    tokens.append(int(num))
    
    # 순차 계산
    result = tokens[0]
    for i in range(1, len(tokens), 2):
        op, nxt = tokens[i], tokens[i + 1]
        if op == '+':
            result += nxt
        elif op == '-':
            result -= nxt
        else:  # '*'
            result *= nxt

    max_val = max(max_val, result)

print(max_val)