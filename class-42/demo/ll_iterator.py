# Given a ll of numbers, sum the numbers
# Warmup
class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next

        return value_generator()

    def __len__(self):
        return len(list(iter(self)))

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


if __name__ == "__main__":
    pass


    # def gen():
    #     for i in range(10):
    #         yield i

    # num_gen = gen()
    # print(num_gen)
    # print(next(num_gen))
    # try:
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    #     print(next(num_gen))
    # except StopIteration:
    #     print('All Done')

    def sum_values(ll):
        current = ll.head
        total = 0
        while current:
            total += current.value
            current = current.next
        return total
