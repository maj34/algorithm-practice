As, At = input().split()
Bs, Bt = input().split()
Cs, Ct = input().split()

arr = [0, 0, 0, 0]
def covid(symptom, temperature):
    if symptom=="Y" and temperature>=37:
        arr[0]+=1
    elif symptom=="N" and temperature>=37:
        arr[1]+=1
    elif symptom=="Y" and temperature<=37:
        arr[2]+=1
    else:
        arr[3]+=1

covid(As, int(At))
covid(Bs, int(Bt))
covid(Cs, int(Ct))

print(*arr, end=" ")

if arr[0]>=2:
    print("E")