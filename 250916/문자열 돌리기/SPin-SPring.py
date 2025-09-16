char = input()

for i in range(len(char)+1):
    print(char[-i:] + char[:-i])