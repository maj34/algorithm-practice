n = int(input())
arr = [input() for _ in range(n)]

max_digit = len(max(arr, key=len))
arr_list = [m.zfill(max_digit) for m in arr]

num_list = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            is_true = True
            for l in range(max_digit):
                if int(arr_list[i][l]) + int(arr_list[j][l]) + int(arr_list[k][l]) >= 10:
                    is_true = False
                    break

            if is_true:
                num_list.append(int(arr_list[i]) +  int(arr_list[j]) + int(arr_list[k]))

if len(num_list) != 0:
    print(max(num_list))
else:
    print(-1)