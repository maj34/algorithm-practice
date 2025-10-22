n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_dist_sq = float('inf')

for i in range(n):
    for j in range(i + 1, n): 
        p1 = points[i]
        p2 = points[j]
        
        dist_sq = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        
        if dist_sq < min_dist_sq:
            min_dist_sq = dist_sq

print(min_dist_sq)