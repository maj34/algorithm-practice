Y, M, D = map(int, input().split())

def leap_year(Y):
    if Y % 4 == 0 and Y % 100 == 0 and Y % 400 == 0:
        return True
    elif Y % 4 == 0 and Y % 100 == 0:
        return False
    elif Y % 4 == 0:
        return True
    else:
        return False

def season(M):
    if 3 <= M <= 5:
        return "Spring"
    elif 6 <= M <= 8:
        return "Summer"
    elif 9 <= M <= 11:
        return "Fall"
    elif 1 <= M <= 2 or M == 12:
        return "Winter"

def existing_day(Y, M, D):
    if M in [1, 3, 5, 7, 8, 10, 12] and D in [i for i in range(1, 32)]:
        return season(M)
    if M in [4, 6, 9, 11] and D in [i for i in range(1, 31)]:
        return season(M)
    if M == 2 and leap_year(Y) and D in [i for i in range(1, 30)]:
        return season(M)
    if M == 2 and leap_year(Y)==False and D in [i for i in range(1, 29)]:
        return season(M)
    return -1

print(existing_day(Y, M, D))
