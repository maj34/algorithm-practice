m1, d1, m2, d2 = map(int, input().split())

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day_num = (sum(day[:m2-1]) + d2) - (sum(day[:m1-1]) + d1)
print(day_week[day_num%7])