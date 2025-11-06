from collections import Counter

X, Y = map(int, input().split())

def is_interesting(n):
    s = str(n)
    k = len(s)
    counts = Counter(s)
    
    return len(counts) == 2 and counts.most_common(1)[0][1] == k - 1

total_count = 0
for i in range(X, Y + 1):
    if is_interesting(i):
        total_count += 1

print(total_count)