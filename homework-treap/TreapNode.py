class TreapNode:
    """
        Node of a treap where bkey = BST key and hkey = heap key
    """

    def __init__(self, bkey=None, hkey=None):
        self.left = None
        self.right = None
        self.parent = None
        self.bkey = bkey
        self.hkey = hkey

    # GETTERS / SETTERS

    def getHkey(self):
        return self.hkey

    def getBkey(self):
        return self.bkey

    def setHkey(self, key):
        self.hkey = key

    def setBkey(self, key):
        self.bkey = key

    def setParent(self, node):
        self.parent = node

    def getParent(self):
        return self.parent

    def setLeft(self, node):
        self.left = node

    def getLeft(self):
        return self.left

    def setRight(self, node):
        self.right = node

    def getRight(self):
        return self.right

    def isRightChild(self):
        return self == self.parent.getRight()

    def __str__(self):
        left = ""
        right = ""
        if self.getLeft():
            left = str(self.getLeft())
        if self.getRight():
            right = str(self.getRight())

        return "(" + left + " " + str(self.bkey) + "," + str(self.hkey) + " " + right + ")"
        # return "("+left+" "+str(self.bkey)+" "+right+")"
