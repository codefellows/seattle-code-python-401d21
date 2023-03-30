# Given a list, sum all the values that are odd.
def sum_odds(lst):
    odd_sum = 0
    for odd in lst:
        if odd % 2 != 0:
            odd_sum += odd
    return odd_sum


# Refactor the problem domain to take a linked-list

def sum_odds_ll(ll): # change the parameter to a ll
    odd_sum = 0
    current = ll.head # now need to work with head of ll
    while current:
        if current.value % 2 != 0:
            odd_sum += current.value
        current = current.next
    return odd_sum

