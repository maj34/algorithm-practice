M, D = map(int, input().split())

def existing_day(M, D):
    if M in [1, 3, 5, 7, 8, 10, 12] and D in [i for i in range(1, 32)]:
        return "Yes"
    if M in [4, 6, 9, 11] and D in [i for i in range(1, 31)]:
        return "Yes"
    if M == 2 and D in [i for i in range(1, 29)]:
        return "Yes"
    return "No"

print(existing_day(M, D))