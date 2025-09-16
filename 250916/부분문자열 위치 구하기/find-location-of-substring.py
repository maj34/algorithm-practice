input_str = input()
target_str = input()

if target_str in input_str:
    print(input_str.index(target_str))
else:
    print(-1)