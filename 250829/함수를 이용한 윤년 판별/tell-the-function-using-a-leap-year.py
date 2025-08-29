y = int(input())

def leap_year(y):
    if y % 100 == 0 and y % 400 != 0:
        return "false"
    elif y % 4 == 0:
        return "true"
    return "false"

print(leap_year(y))