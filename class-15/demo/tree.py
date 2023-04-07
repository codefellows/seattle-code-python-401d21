class Node:
    """
    Docstring
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """
    Docstring
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self, values=[]): #[4, 7, 3, 1, 18, 5, 11]
        # root >> left >> right
        # tree.root = 4
        #                       4
        #                     /   \
        #                   7      18
        #                 /   \   /   \
        #                3     1 5     11

        # expected   [4, 7, 3, 1, 18, 5, 11]
        # walk_through [4, 7, 3, 1, 18, 5, 11]
        def walk(input_node, value_list):
            if not input_node:
                return
            # Do something with the root
            value_list.append(input_node.value)
            # Do something with root.left
            walk(input_node.left, value_list)
            # Do something with root.right1
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def in_order(self):
        # left >> root >> right
        pass

    def post_order(self):
        # left >> right >> root
        pass


class BinarySearchTree(BinaryTree):
    """
    Docstring
    """

    def add(self):
        pass

    def contains(self):
        pass


if __name__ == '__main__':
    #                       4
    #                     /   \
    #                   7      18
    #                 /   \   /   \
    #                3     1 5     11
    # expected   [4, 7, 3, 1, 18, 5, 11]
    bt = BinaryTree()
    node3 = Node(3)
    node1 = Node(1)
    node7 = Node(7, node3, node1)
    node5 = Node(5)
    node11 = Node(11)
    node18 = Node(18, node5, node11)
    node4 = Node(4, node7, node18)
    bt.root = node4
    print(bt.pre_order())
