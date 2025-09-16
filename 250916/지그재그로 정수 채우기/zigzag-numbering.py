N, M = map(int, input().split())

arr = [
    [0 for _ in range(M)]
    for _ in range(N)
]

num = 0
for col in range(M):
    if col%2==0:
        for row in range(N):
            arr[row][col] = num
            num += 1
    else:
        for row in range(N-1, -1, -1):
            arr[row][col] = num
            num += 1
# 출력
for row in range(N):
    for col in range(M):
        print(arr[row][col], end=" ")
    print()

# arr = []
# num = 0
# for i in range(N):
#     for j in range(M):
#         arr.append(num)
#         num += 1
# # print(arr)

# num = 0
# for i in range(M):
#     if i%2==0:
#         for j in range(N):
#             print(num, end=" ")
#             num += 1
#         print()
#     else:
#         for k in range(M, M-N, -1):
#             print(num, end=" ")
#             num += 1
#         print()

# num = 0
# for i in range(N):
#     for j in range(M):
#         if i%2==0 and j%2==0:
#             print(num)
#             num += (N*2-1)
#         elif i%2==0 and j%2!=0:
#             print(num)
#             num += 1