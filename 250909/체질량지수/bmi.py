h, w = map(int, input().split())

bmi = (10000*w) / (h*h)

if bmi >= 25:
    print(int(bmi))
    print("Obesity")
else:
    print(int(bmi))