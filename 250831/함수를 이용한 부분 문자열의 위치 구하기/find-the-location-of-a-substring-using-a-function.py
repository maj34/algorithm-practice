text = input()
pattern = input()

def char_index(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        if pattern not in text:
            return -1
        else:
            return text.index(pattern)
        
print(char_index(text, pattern))
        
    