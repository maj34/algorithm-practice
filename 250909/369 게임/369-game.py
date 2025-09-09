N = int(input())

for i in range(1, N+1):
    if i % 3 == 0:
        print(0, end=" ")
    else:
        has_369 = False
        for j in str(i):
            if j in ["3", "6", "9"]:
                print(0, end=" ")
                has_369 = True
                break
        if not has_369:
            print(i, end=" ")