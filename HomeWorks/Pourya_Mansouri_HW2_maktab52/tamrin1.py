# reverse function
def reverse_string(input_string: str) -> str:
    return input_string[::-1]


# is_palindrome function
def is_palindrome(input_string: str) -> bool:
    if input_string == reverse_string(input_string):
        return True
    return False


# main
if __name__ == '__main__':
    input_string = input()
    if is_palindrome(input_string):
        print("true")
    else:
        print('false')
