A = input()

def unique_char(A):
    if len(set(A)) >= 2:
        return "Yes"
    return "No"

print(unique_char(A))