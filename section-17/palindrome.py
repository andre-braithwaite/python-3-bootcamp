def is_palindrome(string):
    forwards = [_.lower() for _ in string if _ != ' ']
    backwards = reversed(forwards)
    
    print(forwards)
    print(backwards)

    if forwards == backwards:
        return True
    return False

print(is_palindrome('tacocat'))