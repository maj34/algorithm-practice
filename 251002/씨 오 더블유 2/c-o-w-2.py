n = int(input())
S = input()

c_idx, o_idx, w_idx = [], [], []

for idx in range(n):
    if S[idx] == "C":
        c_idx.append(idx)
    elif S[idx] == "O":
        o_idx.append(idx)
    elif S[idx] == "W":
        w_idx.append(idx)

cnt = 0
for i in c_idx:
    for j in o_idx:
        for k in w_idx:
            if i < j < k:
                cnt += 1

print(cnt)