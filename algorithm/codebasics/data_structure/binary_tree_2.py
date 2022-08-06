class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:  # recursion breaks here
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, value):
        if self.data == value:  # recursion breaks here
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False  # recursion breaks here if the first one did not break it

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False  # recursion breaks here if the first two did not break it

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete_node(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete_node(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete_node(min_value)
        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 28, 9, 23, 18, 34, 56, 90, 90]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    # numbers_tree.delete_node(28)
    # print(numbers_tree.in_order_traversal())
    numbers_tree.delete_node(34)
    print(numbers_tree.in_order_traversal())

    # countries = ['India', 'Pakistan', 'China', 'Germany', 'Nigeria', 'usa', 'ak']
    # countries_tree = build_tree(countries)
    # print(countries_tree.in_order_traversal())
    # print(countries_tree.search('AK'))
    # print(countries_tree.search('USA'))
    # print(countries_tree.search('usa'))
