char = list(input())

print(''.join(char[:char.index('e')] + char[char.index('e')+1:]))