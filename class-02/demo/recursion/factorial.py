def factorial(num):
    """
    Take in a number and multiple that number by every number -1
    factorial(2)
    ex: factorial(3) = 3 * 2 * 1 = 6
    1 * 2
    :return:
    n * (n - 1)
    """

    if num <= 1:
        return 1

    return num * factorial(num - 1)


# factorial(3)
# 3 * factorial(3 - 1) -> 6
# 3 * 2
#  factorial(2) -> 2
# 2 * 1
# 2 * factorial(2 - 1) -> 1
# factorial(1)
# returns 1


# factorial(3)
# factorial(2)
# factorial(1)

