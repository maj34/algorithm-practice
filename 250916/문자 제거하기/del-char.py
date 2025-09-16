char = list(input())

for _ in range(20):
    idx = int(input())
    if idx < len(char):
        char.pop(idx)
        print(''.join(char))
    else: 
        char.pop(len(char)-1)
        print(''.join(char))

    if len(char) == 1:
        break