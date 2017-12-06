class TreapNode:
    """
        Key = BST value
        Value = Heap value
    """
    def __init__(self,key,value,left=None,right=None,parent=None):

        self.left = left
        self.right = right
        self.parent = parent

        self.key = key
        self.value = value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def setLeft(self,new):
        self.left = new

    def setRight(self):
        self.right = new

    def setParent(self):
        self.parent = new

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value
