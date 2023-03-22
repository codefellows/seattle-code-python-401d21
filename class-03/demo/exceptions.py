#
# print("let's do something totally wrong. see if you can spot the output error")
# print('Hi')
#
#
# print("What happens now?")
try:
    value = 1/0
except ZeroDivisionError:
    print('Cannot divide my 0 you fool.')
else:
    print('Everything looks good')
finally:
    print('This will always print')

# try:
#     print("Do not devide by 0:", 1 / '0')
# except:
#     print('Do not divide by 0')


# try:
#     spam = 'junk' / 42
# except ZeroDivisionError:
#     print('Do not divide by zero')
# except Exception as a:
#     print(a)

# age = 20
#
# if age < 21:
#     raise ValueError('Not old enough. Gotta be 21')
