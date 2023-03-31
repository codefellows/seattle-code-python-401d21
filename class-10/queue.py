class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None):
        self.front = front
        self.back = None
        pass

    def enqueue(self, value):
        # adding to the back of the queue
        # if the queue is empty, the new node becomes the front and the back.
        node = Node(value)
        # check if the queue is empty
        self.back._next = node
        self.back = node
        if not self.front:
            self.front = node


class Node:
    def __int__(self, value, _next=None):
        self.value = value
        self._next = _next
