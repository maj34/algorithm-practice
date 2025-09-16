S, Q = input().split()
S = list(S)

for _ in range(int(Q)):
    arr = list(input().split())

    if arr[0] == "1":
        first = S[int(arr[1])-1]
        second = S[int(arr[2])-1]
        S[int(arr[1])-1] = second
        S[int(arr[2])-1] = first
        print(''.join(S))

    elif arr[0] == "2":
        char = arr[1]
        for i in range(len(S)):
            if S[i] == char:
                S[i] = arr[2]
        print(''.join(S))