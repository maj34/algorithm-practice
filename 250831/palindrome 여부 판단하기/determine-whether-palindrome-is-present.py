A = input()

def is_palindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            return "No"
    return "Yes"

print(is_palindrome(A))