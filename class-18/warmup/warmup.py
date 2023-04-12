# Feature Tasks
# This is the result of your breath-first-search:
# ["a","b","c","d","e","f"]

# Ideas to accomplish this?
# move from list to stack
    # pop off stack until none and print each time
# insert list into a LL
    # traverse through the ll and print each value
# insert to a LL. traverse throught the ll and enqueue to queue
    # the dequeue and print
# add to a ll.  Then enqueue.  Dequeue to a stack.  Print from stack

# list into a stack - enqueue to queue then dequeue

# put into a ll then reverse the ll and then traverse.

dfs = ["a","b","c","d","e","f"]

def reverse_print1(lst):
    stack = Stack()
    for item in lst:
        node = Node(item)
        stack.push(node)

    while stack:
        print("1")

print(stack)
print(stack.top)
