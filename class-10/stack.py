class Stack:
    """
    Put docstring here
    """


    def __init__(self, top=None):
        # initialization here
        self.top = top


    def push(self, value):
        # method body here
        node = Node(value)
        node._next = self.top
        self.top = node



class Node:
    def __int__(self, value, _next=None):
        self.value = value
        self._next = _next
