# file = open('assets/spam.txt')
# print(file)

# contents = file.read()
# print(contents)
#
# print('Is the file closed', file.closed)
# file.close()
# print('Is the file closed', file.closed)

with open('assets/spam.txt') as file:
    # print(file.read())
    context = file.read()
    # print(help(file))
# print('Is the file closed', file.closed)

# with open('assets/brain.jpg', 'rb') as original:
#     contents = original.read()
#
# with open('assets/brain.copy.jpg', 'wb') as copied_file:
#     copied_file.write(contents)
#
# for pixel in contents:
#     print(pixel)

for char in context:
    print(char)
