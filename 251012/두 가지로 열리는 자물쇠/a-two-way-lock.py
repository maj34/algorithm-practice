N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

llst = [i for i in range(1, N+1)]

def valid_dial(num):
    lst = []
    for i in range(-2, 3):
        tmp = (llst.index(num)+i) % N
        lst.append(llst[tmp])
    return lst

a1_lst, b1_lst, c1_lst = valid_dial(a1), valid_dial(b1), valid_dial(c1)
a2_lst, b2_lst, c2_lst = valid_dial(a2), valid_dial(b2), valid_dial(c2)

valid_set = set()
for i in a1_lst:
    for j in b1_lst:
        for k in c1_lst:
            valid_set.add((i, j, k))

for i in a2_lst:
    for j in b2_lst:
        for k in c2_lst:
            valid_set.add((i, j, k))

print(len(valid_set))