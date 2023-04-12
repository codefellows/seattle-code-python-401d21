# `IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV`
#  The quick brown fox jumped over the lazily sleeping dog
# E A T O N R I S H
# Shift 11
# write an encrypt function that will shift numbers by a "shift value"

# Input Number, shift value  -> 55 shift of 3 -> 88
# Output  numer that is shifted -> 88

# Verify Getting a number
# numbers 1 - 0 wrap around on numbers 123456789012345

# number: 890 shift 3
# 123

# create function that takes number and a shift value
    # convert number to string
    # create temp string
    # interate though the string
        # shift the value by the shift value
            # Check if greater than 10
        # concate that value to my temp string
    # convert temp back to number
    # retrun the number

# Number is the item to shift
# key is the value to shifty by
# 890 - '890'
def encrypt(num, key):
    strng_num = str(num)
    temp_string = ''
    for char in strng_num:
        int_num = int(char)
        shifted_number = int_num + key
        # while shifted_number >= 10:
        #     shifted_number -= 10
        shifted_number = shifted_number % 10
        temp_string += str(shifted_number)
    temp_string = int(temp_string)
    return temp_string


if __name__ == '__main__':
    print(encrypt(890, 3)) # 123
    print(encrypt(66, 3)) # 99
    print(encrypt(199, 219875)) # 644
    print(encrypt(123, -3))
    print(encrypt(99, -33)) # 99
    print(encrypt(644, -219875)) #
