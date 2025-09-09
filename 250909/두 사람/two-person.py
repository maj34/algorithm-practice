age1, gender1 = input().split()
age2, gender2 = input().split()

if int(age1) >= 19 and gender1 == "M":
    print(1)
elif int(age2) >= 19 and gender2 == "M":
    print(1)
else:
    print(0)