# Given a string, write a function that returns a new string but only has one of each character
# Exampe: 'commissioner'
# Return: 'comisner'

def check_string(string):
    new_string = ''
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string


if __name__ == '__main__':
    my_string = 'commissioner'
    print(check_string(my_string))
