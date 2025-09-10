age_sum = 0
num = 0

while True:
    age = int(input())
    if age<30:
        age_sum+=age
        num+=1
    else:
        print(f"{age_sum/num:.2f}")
        break