k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

ranks = [[0] * (n + 1) for _ in range(k)]

for i in range(k):
    for j in range(n):
        dev_id = arr[i][j]
        ranks[i][dev_id] = j

count = 0

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            continue
            
        a_always_wins = True
        for i in range(k):
            if ranks[i][a] > ranks[i][b]:
                a_always_wins = False
                break 
        
        if a_always_wins:
            count += 1

print(count)