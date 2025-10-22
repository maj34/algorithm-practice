N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

max_students = 0

for i in range(N):
    temp_P = []
    for j in range(N):
        if i == j:
            temp_P.append(P[j] / 2)
        else:
            temp_P.append(P[j])
            
    temp_P.sort()
    current_sum = 0
    count = 0
    for price in temp_P:
        if current_sum + price <= B:
            current_sum += price
            count += 1
        else:
            break
            
    max_students = max(max_students, count)

print(max_students)