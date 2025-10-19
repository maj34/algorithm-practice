n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

max_area2 = 0  # 면적 * 2 값 저장

for ax, ay in points:
    # A를 기준으로 같은 x와 y를 공유하는 점들을 찾음
    same_x = [by for (bx, by) in points if bx == ax and by != ay]
    same_y = [cx for (cx, cy) in points if cy == ay and cx != ax]
    
    for by in same_x:
        for cx in same_y:
            width = abs(cx - ax)
            height = abs(by - ay)
            area2 = width * height
            max_area2 = max(max_area2, area2)

print(max_area2)