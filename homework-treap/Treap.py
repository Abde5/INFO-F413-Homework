from TreapNode import TreapNode
import random

class Treap:
    """
        Class that implements the random treap
    """

    def __init__(self):
        self.root = None

    def insert(self,elem):

        # BST step
        attach = self.find(elem,False)

        node = TreapNode(elem,random.random())

        if attach == None:
            self.root = node
            return

        node.setParent(attach)
        if elem <= attach.getBkey() :
            attach.setLeft(node)
        else:
            attach.setRight(node)

        # Heap step


    def delete(self,elem):
        pass

    def find(self,elem,finding=True):
        """
            Returns node such that "elem" value == node. Or the node where it stops.
        """

        previous = None
        current = self.root

        while current != None:
            previous = current
            if finding:
                if elem == current.getBkey() :
                    break
            if elem <= current.getBkey() :
                current = current.getLeft()
            else:
                current = current.getRight()

        return current if current != None else previous


    def rightRotation(self,node):
        """
            Performs a right rotation, supposes that node is a leftChild.
        """

        parent = node.getParent()
        right = node.getRight()

        node.setParent(parent.getParent())
        parent.setParent(node)
        right.setParent(parent)
        parent.setLeft(right)

        if node.getParent():
            if node.getParent().getRight() == parent:
                node.getParent().setRight(node)
            else:
                node.getParent().setLeft(node)


    def leftRotation(self,node):
        """
            Performs a left rotation, supposes that node is a rightChild.
        """

        parent = node.getParent()
        left = node.getLeft()

        node.setParent(parent.getParent())

        parent.setParent(node)
        node.setLeft(parent)

        left.setParent(parent)
        parent.setRight(left)

        if node.getParent():
            if node.getParent().getRight() == parent:
                node.getParent().setRight(node)
            else:
                node.getParent().setLeft(node)

    def __str__(self):
        return str(self.root)
