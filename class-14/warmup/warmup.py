# Given a linkedlist where the data of each node is a list, return the value
# furthest removed from 0.
# ll: ( [2, 8, -2] ) -> ( [-1, -22, 21] ) -> None
#        ^
# Expected output: -22

def furthest_from_zero(ll):
    # Set the furthest variable
    furthest = 0
    # Set the current variable
    current = ll.head
    # Traverse the LL
    while current:
        # Loop through the List
        for num in current.value:
            if abs(num) > abs(furthest):
                furthest = num
        # assign the furthest from 0 to variable furthest

        current = current.next
    return furthest

