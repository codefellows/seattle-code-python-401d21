def largest_value(ll):
    """
    Function that will traverse the ll.
    :param ll: linked list of integers
    :return: the largest integer
    """
    # ll: (7) -> (2) -> (13) -> (9) -> (3) -> None
    #                                          ^
    # highest: 13
    # This assigns current to the node at the head of the ll
    current = ll.head
    # This variable will trace the highest value
    highest = current.value
    while current is not None:
        if current.value > highest:
            highest = current.value
        current = current.next
    return highest

# correct: ll.head.value
# incorrect: ll.value


    # ll: (7) -> (2) -> (13) -> (9) -> (3) -> ((15)) -> None

    # append 15
