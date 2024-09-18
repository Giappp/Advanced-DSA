# The Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.red = False


# Red-black properties:
# 1. Every Node is either red or black
# 2. The root is black
# 3. Every leaf(Null) is black
# 4. If a node is red, then both its children are black
# 5. For each node, all simple path from its descendant to its leaves contain the same number of black nodes
class RedBlackTree:
    def __init__(self):
        # Color of the Node either Red or Black
        self.nil = Node(0)  # The nil node, represents nothing
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        # The parent node
        self.root = self.nil  # The root of all node is NIL

    #       y                                  x
    #      / \          Left Rotation         / \
    #     x   S1        <-------------       S2  y
    #    / \                                    / \
    #   S2  S3                                 S3  S1

    # Left Rotation: Promotes the right child of a node
    # and demotes the node itself to the left child of its former right child.
    # Only pointers are changed by a rotation, all other attribute in a node remain the same
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:  # If y's subtree is not empty
            y.left.parent = x  # ... then x becomes the parent of the subtree's root (S3)
        y.parent = x.parent  # x's parent becomes y's parent
        if x.parent == self.nil:  # If x was the root
            self.root = y  # ... then y becomes the root
        elif x == x.parent.left:  # otherwise, if x was the left child
            x.parent.left = y  # then y becomes a left child
        elif x == x.parent.right:  # otherwise, x was a right child so now y becomes the right child
            x.parent.right = y
        y.left = x  # Make x becomes y's left child
        x.parent = y  # Now y is the parent of x

    #       y                                   x
    #      / \          Right Rotation         / \
    #     x   S1        ------------->       S2   y
    #    / \                                     / \
    #   S2  S3                                  S3  S1

    # Right Rotation: Promotes the left child of a node
    # and demotes the node itself to the right child of its former left child.
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:  # If x's right subtree is not empty
            x.right.parent = y  # then y become the parent of that subtree (S3)
        x.parent = y.parent  # x's current parent becomes y's parent
        if x.parent == self.nil:  # If x was the root
            self.root = x
        elif x == x.parent.left:  # If x was the left child
            x.parent.left = y  # then y becomes a left child
        elif x == x.parent.right:  # otherwise
            x.parent.right = y
        x.right = y
        y.parent = x

    def insert(T, z):
        # T is the red-black tree
        x = T.root  # Node being compared with z
        y = T.nil  # y will be parent of z
        while x != T.nil:  # Descend until reaching the sentinel
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y  # Found the location - insert z with parent y
        if y == T.nil:
            T.root = z  # tree T was empty
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = T.nil  # Both of z's children are the sentinel
        z.right = T.nil
        z.red = True  # the new node starts out red
        T.insert_fixup(T, z)  # Correct any violations of red-black tree

    def insert_fixup(T, z):
        pass
