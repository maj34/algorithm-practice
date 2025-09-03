m1, d1, m2, d2 = map(int, input().split())

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print((sum(day[:m2-1])+d2) - (sum(day[:m1-1])+d1) + 1)