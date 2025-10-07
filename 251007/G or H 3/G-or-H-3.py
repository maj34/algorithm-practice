n, k = map(int, input().split())
# x = []
# c = []
# for _ in range(n):
#     pos, char = input().split()
#     x.append(int(pos))
#     c.append(char)

pos_dict = {}
for _ in range(n):
    pos, char = input().split()
    pos_dict[int(pos)] = char
pos_dict = dict(sorted(pos_dict.items()))
pos_keys = pos_dict.keys()

max_point = 0
for i in range(n):
    point = 0
    for j in range(i, n):
        if abs(list(pos_keys)[j] - list(pos_keys)[i]) <= k:
            if pos_dict[list(pos_keys)[j]] == "G":
                point += 1
            elif pos_dict[list(pos_keys)[j]] == "H":
                point += 2
            max_point = max(max_point, point)

print(max_point)