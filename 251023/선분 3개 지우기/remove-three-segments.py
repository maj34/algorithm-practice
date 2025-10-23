from itertools import combinations

n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

def is_overlap(i, j):
    return not (r[i] < l[j] or r[j] < l[i])

def non_overlap(indices):
    for a in range(len(indices)):
        for b in range(a + 1, len(indices)):
            if is_overlap(indices[a], indices[b]):
                return False
    return True

ans = 0
for remove in combinations(range(n), 3):      
    remain = [i for i in range(n) if i not in remove]
    if non_overlap(remain):
        ans += 1

print(ans)