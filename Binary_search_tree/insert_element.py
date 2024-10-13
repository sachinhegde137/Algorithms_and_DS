
def pre_order(root):
    if root == None:
        return
    print (root.value, end=" ")
    pre_order(root.left)
    pre_order(root.right)

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        curr = self.root
        while curr is not None:
            if value < curr.value:
                if not curr.left:
                    curr.left = Node(value)
                    break
                curr = curr.left
            elif value > curr.value:
                if not curr.right:
                    curr.right = Node(value)
                    break
                curr = curr.right
            else:
                break


    def create(self, int_list):
        for num in int_list:
            self.insert(num)


if __name__ == "__main__":
    num_list = [4, 2, 7, 1, 3]

    tree = BinarySearchTree()

    tree.create(num_list)
    pre_order(tree.root)