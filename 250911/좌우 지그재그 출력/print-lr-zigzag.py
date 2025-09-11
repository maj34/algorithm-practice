N = int(input())

# num = 1
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i%2!=0:
#             print(i+j, end="")
#         else:
#             num+=N
#             print(i-j, end="")
#     print()

num = 1
for i in range(N):
    tmp = []
    for j in range(N):
        if i%2==0:
            print(num, end=" ")
            num += 1
        else:
            if j < N-1:
                tmp.append(num)
                num += 1
            else:
                tmp.append(num)
                num += 1
                for k in list(reversed(tmp)):
                    print(k, end=" ")
    print()