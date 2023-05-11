"""
Given a list of linked-lists with values of single, positive integers, create a function to traverse the list and convert the list to a number, add the lists together and return the total value of all lists.

The lists will be passed as parameters.
[ll1, ll2, ll3]
       ^
ll1: [5]->[9]->[9] -> None = 599
                      ^
ll2: [2]->[1]->[1] = 211
     ^
ll3: [1]->[4]->[1] = 141
total 599 + 211 +141
list_num '141'
Should return 951
"""

def add_ll(lst):
    # Assign total var to 0
    total  = 0
    # Check for empty list ? return 0
    if len(lst) == 0:
        return total
    # iterate through the list of ll
    for ll in lst:
        # set list_number string
        list_num = ''
        # assign current
        current = ll.head
        # traverse through the ll
        while current:
            # cocat the str of value to the list_number
            list_num += str(current.value)
            current = current.next

        # add int of list_number to total
        total += int(list_num)
    # return total
    return total
