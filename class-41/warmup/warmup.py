"""
 Given a linked-list of objects, with an age property, and a target age, find the age that is closest in age to the target age.

 Assumptions:
 There will always be a valid-linked list.
 There will always be at least 1 node in the ll.
 Three will always be a properly formatted object.
 There will not 2 values that are same from target.
    - given 15 as a target , will not have ages of 10 and 20.

 Input:
 {age:47,...}, {age:23,...}, {age: 17}
 Target Age: 29
 Expected Output: 23
"""

def find_age_ll(ll, target_age):
    # closest= None
    closest = None
    # set a prev diff set to ~
    prev_diff = float("inf")
    # set a variable t the head of the ll
    current = ll.head
    # A while loop to travers through the ll
    while current:
    #     - assign a diff to abs value of value.age - target age
        print('Current_age', current.value["age"])
        diff = abs(current.value["age"] - target_age)
    #    - check the dff between current.value(age property from the object) and prev diff
        if diff < prev_diff:
            print('Diff',diff)
            print('Prev_diff',prev_diff)
        # - Clarify:  difference between current and target?
            closest = current.value["age"]
            print('closest', closest)
            prev_diff = diff
    #    - if dif < pre diff
        current = current.next
    #    - reassign closest variable to the actual age
    return closest



class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

class LinkedList:
    def __init__(self, head=None):
        self.head = head


if __name__ == '__main__':
    #  {age:47,...}, {age:23,...}, {age: 17}
    age = 29
    node1 = Node({"age": 17})
    node2 = Node({"age": 23}, node1)
    node3 = Node({"age": 47}, node2)
    ll1 = LinkedList(node3)
    print(f'The closest age to {age} is : {find_age_ll(ll1, age)}')
