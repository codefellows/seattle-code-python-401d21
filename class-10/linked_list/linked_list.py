class LinkedList:
    """
    A singly-linked list.

    Attributes:
        head (Node): The first node in the linked list.
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self): # Same as to_string
        current = self.head
        output_msg = ''
        while current:
            output_msg += f' { {current.value} } -> '
        output_msg += ' None'

    # LL: (3) -> (8) -> (2) -> None
    #                           ^
    # Head : 2
    # Current : 1
    def traverse_list(self):
        current = self.head
        while current is not None:
            current.value += 1
            current = current.next
        return "something"

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current._next
        return False

    def append(self, value):
        current = self.head
        while current.next:
            current = current._next
        node = Node(value)
        current.next = node

    def insert_before(self, value, new_value):
        node = Node(new_value)
        current = self.head
        while current.next.value != value or current is None:
            current = current.next
        if current is None:
            raise TargetError
        temp = current.next
        current.next = node
        node.next = temp

    def insert_after(self, value, new_value):
        node = Node(new_value)
        current = self.head
        while current.value != value or current is None:
            current = current.next
        if current is None:
            raise TargetError
        temp = current.next
        current.next = node
        node.next = temp

    def kth_from_end(self, k):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        current = self.head
        steps_remaining = length - k - 1
        if steps_remaining < 0:
            raise TargetError
        for _ in range(steps_remaining):
            current = current.next
            if not current:
                raise TargetError
        return current.value

class Node:
    """
    A node in a singly-linked list.

    Attributes:
        value (any): The value stored in the node.
        next (Node): The next node in the list.
    """
    def __init__(self, value, _next=None):
        # value, next
        self.value = value
        self._next = _next
    # Node(3, node2)
    # Node.value = 3
    # Node._next = node2


class TargetError(Exception):
    pass


def zip_linked_lists(ll1, ll2):

    current_1 = ll1.head
    current_2 = ll2.head

    while current_1 and current_2:
        next_1 = current_1.next
        next_2 = current_2.next
        current_1.next = current_2
        if next_1:
            current_2.next = next_1
        current_1 = next_1
        current_2 = next_2

    return ll1 if ll1.head else ll2
