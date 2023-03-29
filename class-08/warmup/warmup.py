def squares1():
    nums = (1,2,3,4,5)
    squares = [num ** 2 for num in nums]
    assert squares == [1,4,9,16,25]


def squares2():
    nums = (1,2,3,4,5)
    squares = []
    for num in nums:
        squares.append(num ** 2)
    assert squares == [1,4,9,16,25]

squares1()
squares2()
