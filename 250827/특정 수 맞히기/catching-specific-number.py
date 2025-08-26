n = int(input())

while True:
    if n == 25:
        print("Good")
        break
    elif n > 25:
        print("Lower")
        n = int(input())
    elif n < 25:
        print("Higher")
        n = int(input())
    else:
        continue