
class binaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def addLeft(self, item):
        assert self.left_child is None, "Left child already exist"
        new = binaryTree(item)
        self.left_child = new
        return new.data+" has been added"

    def addRight(self, item):
        assert self.right_child is None, "Right child already exist"
        new = binaryTree(item)
        self.right_child = new
        return new.data+" has been added"

    def delLeft(self):
        assert self.left_child is not None, "left child not Exist"
        assert self.left_child.left_child is None, "Can't delete this node"
        temp = self.left_child.data
        self.left_child = None
        return temp+" has been deleted"

    def traverse_in(self):
        if self.left_child is not None:
            self.left_child.traverse_in()

        print(self.data, end=" ")

        if self.right_child is not None:
            self.right_child.traverse_in()

    def traverse_pre(self):
        print(self.data, end=" ")

        if self.left_child is not None:
            self.left_child.traverse_pre()

        if self.right_child is not None:
            self.right_child.traverse_pre()

    def traverse_post(self):
        if self.left_child is not None:
            self.left_child.traverse_post()

        if self.right_child is not None:
            self.right_child.traverse_post()

        print(self.data, end=" ")

    def traverse_bf(self):
        nodes = [self]
        print(self.data, end=" ")

        while nodes:
            p = nodes.pop(0)
            if p.left_child is not None:
                print(p.left_child.data, end=" ")
                nodes.append(p.left_child)
            if p.right_child is not None:
                print(p.right_child.data, end=" ")
                nodes.append(p.right_child)
        print()

    def height(self):
        height_left = 0
        height_right = 0
        if self is None:
            return 0
        else:
            if self.left_child is not None:
                height_left = self.left_child.height()
            if self.right_child is not None:
                height_right = self.right_child.height()
            if height_left > height_right:
                return height_left + 1
            else:
                return height_right+1

    def count_nodes(self):
        if self.left_child is None and self.right_child is None:
            return 1

        left_nodes = right_nodes = 0

        if self.left_child is not None:
            left_nodes = self.left_child.count_nodes()

        if self.right_child is not None:
            right_nodes = self.right_child.count_nodes()

        return left_nodes + right_nodes + 1

    def count_leaf(self):
        if self.left_child is None and self.right_child is None:
            return 1
        left_leaves = right_leaves = 0
        if self.left_child is not None:
            left_leaves = self.left_child.count_leaf()

        if self.right_child is not None:
            right_leaves = self.right_child.count_leaf()

        return left_leaves + right_leaves
#making tree manually

node1 = binaryTree("A")
node2 = binaryTree("B")
node3 = binaryTree("C")
node4 = binaryTree("D")
node5 = binaryTree("E")
node6 = binaryTree("F")
node7 = binaryTree("G")

node2.left_child = node3
node2.right_child = node4

node5.left_child = node6
node5.right_child = node7

node1.left_child = node2
node1.right_child = node5

#traversing...

print("In Order : ", end=" ")
node1.traverse_in()
print()

print("Pre Order : ", end=" ")
node1.traverse_pre()
print()

print("Post Order : ", end=" ")
node1.traverse_post()
print()

print("Breadth First : ", end=" ")
node1.traverse_bf()
print()

print("Height of tree =",node1.height())
print()
print("Total nodes =",node1.count_nodes())
print()
print("Total leaves =",node1.count_leaf())
print()