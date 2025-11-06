T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

s_points = []
n_points = []
for i in range(T):
    if c[i] == 'S':
        s_points.append(x[i])
    else:
        n_points.append(x[i])

count = 0
for i in range(a, b + 1):
    
    min_s_dist = float('inf')
    for s_pos in s_points:
        min_s_dist = min(min_s_dist, abs(i - s_pos))
        
    min_n_dist = float('inf')
    for n_pos in n_points:
        min_n_dist = min(min_n_dist, abs(i - n_pos))
        
    if min_s_dist <= min_n_dist:
        count += 1

print(count)