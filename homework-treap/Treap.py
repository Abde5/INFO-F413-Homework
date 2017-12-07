from TreapNode import TreapNode
import random


class Treap:
    """
        Class that implements the random treap
    """

    def __init__(self):
        self.root = None

    def insert(self, elem):
        """
            Performs the insert operation with elem as the BST key and a random heap key.
        """

        # BST step
        attach = self.find(elem, False)

        node = TreapNode(elem, random.random())

        if attach == None:
            self.root = node
            return

        node.setParent(attach)
        if elem <= attach.getBkey():
            attach.setLeft(node)
        else:
            attach.setRight(node)

        # Heap step
        while node.getParent() != None and node.getHkey() > node.getParent().getHkey():
            if node.isRightChild():
                self.leftRotation(node)
            else:
                self.rightRotation(node)

    def delete(self, elem):
        """
            Performs de deletion by moving the node to a leaf and deleting it.
        """
        node = self.find(elem)

        if node.getBkey() != elem:
            return

        # moves node down til' it's a leaf
        while node.getLeft() != None or node.getRight() != None:
            left = -1 if node.getLeft() == None else node.getLeft().getHkey()
            right = -1 if node.getRight() == None else node.getRight().getHkey()

            if left > right:
                self.rightRotation(node.getLeft())
            else:
                self.leftRotation(node.getRight())

        # deletes node
        if node.isRightChild():
            node.getParent().setRight(None)
        else:
            node.getParent().setLeft(None)

    def find(self, elem, finding=True):
        """
            Returns node such that "elem" value == node. Or the node where it stops.
        """

        previous = None
        current = self.root

        while current != None:
            previous = current
            if finding:
                if elem == current.getBkey():
                    break
            if elem <= current.getBkey():
                current = current.getLeft()
            else:
                current = current.getRight()

        return current if current != None else previous

    def rightRotation(self, node):
        """
            Performs a right rotation, supposes that node is a leftChild.
        """
        parent = node.getParent()

        if parent == self.root:
            self.root = node

        right = node.getRight()

        node.setParent(parent.getParent())

        parent.setParent(node)
        if right:
            right.setParent(parent)
        node.setRight(parent)

        parent.setLeft(right)

        if node.getParent():
            if node.getParent().getRight() == parent:
                node.getParent().setRight(node)
            else:
                node.getParent().setLeft(node)

    def leftRotation(self, node):
        """
            Performs a left rotation, supposes that node is a rightChild.
        """
        parent = node.getParent()

        if parent == self.root:
            self.root = node

        left = node.getLeft()

        node.setParent(parent.getParent())

        parent.setParent(node)
        if left:
            left.setParent(parent)
        node.setLeft(parent)

        parent.setRight(left)

        if node.getParent():
            if node.getParent().getRight() == parent:
                node.getParent().setRight(node)
            else:
                node.getParent().setLeft(node)

    def getDepth(self, node):
        """
            Returns the depth of a node (distance from the root).
        """

        depth = 1
        while node != self.root:
            depth += 1
            node = node.getParent()
        return depth

    def __str__(self):
        return str(self.root)
