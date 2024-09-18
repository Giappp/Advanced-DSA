class AVLTree:
    def __init__(self, value):
        self.value = value
        self.size = 0
        self.left = None
        self.right = None

    #        Rotate Right          Rotate Left-Right
    #          a(2)                 a(2)
    #         /                    /
    #        b(1)                b(1)
    #       /                        \
    #      c(0)                      c(2)

    # Used when a Node is inserted in the right of AVLTree
    def rotateLeft(y):
        x = y.right
