"""
    Node class the Game Tree class is composed by.
"""
from enum import Enum

class NodeType(Enum):
    NOR = 1
    AND = 2
    OR = 3

class GameTreeNode:
    """
        Represents a node in the GameTree.
    """
    def __init__(self):
        """
          Children can either be a node or a number.
        """
        self.leftChild = None
        self.rightChild = None
        self.direction = None
        self.type = None

    def set_right(self,node):
        self.rightChild = node

    def set_left(self,node):
        self.leftChild = node

    def set_direction(self,direction):
        self.direction = direction

    def set_type(self,_type):
        self.type = _type

    def evaluate(self):
        """
            This method will evaluate the 2 child and then return a tuple
            (result,score) where score is the number of leaves reached.
        """
        if self.type == NodeType.AND:
            return self._and()
        elif self.type == NodeType.OR:
            return self._or()
        elif self.type == NodeType.NOR:
            return self._nor()

    def _and(self):
        """
          AND evaluation between 2 children
        """
        score = 0
        res = True

        children = [self.rightChild,self.leftChild]
        if self.direction:
            children = [self.leftChild,self.rightChild]

        if type(children[0]) == bool:
            score += 1
            if not children[0]:
                res = False
        else:
            ret = children[0].evaluate()
            if not ret[0]:
                res = False
            score += ret[1]

        if res:
            if type(children[1]) == bool:
                score += 1
                if not children[1]:
                    res = False
            else:
                ret = children[1].evaluate()
                if not ret[0]:
                    res = False
                score += ret[1]

        return (res,score)

    def _or(self):
        """
            OR evaluation between 2 children
        """
        score = 0
        res = False

        children = [self.rightChild,self.leftChild]
        if self.direction:
            children = [self.leftChild,self.rightChild]

        if type(children[0]) == bool:
            score += 1
            if children[0]:
                res = True
        else:
            ret = children[0].evaluate()
            if ret[0]:
                res = True
            score += ret[1]

        if not res:
            if type(children[1]) == bool:
                score += 1
                if children[1]:
                    res = True
            else:
                ret = children[1].evaluate()
                if ret[0]:
                    res = True
                score += ret[1]

        return (res,score)

    def _nor(self):
        """
            NOR evaluation between 2 children
        """
        score = 0
        res = True

        children = [self.rightChild,self.leftChild]
        if self.direction:
            children = [self.leftChild,self.rightChild]

        if type(children[0]) == bool:
            score += 1
            if children[0]:
                res = False
        else:
            ret = children[0].evaluate()
            if ret[0]:
                res = False
            score += ret[1]

        if res:
            if type(children[1]) == bool:
                score += 1
                if children[1]:
                    res = False
            else:
                ret = children[1].evaluate()
                #print(ret)
                if ret[0]:
                    res = False
                score += ret[1]

        #print(res,score)
        return (res,score)

    def __str__(self):
        res = ""
        if self.type == NodeType.AND:
            res += "Node AND"
        if self.type == NodeType.OR:
            res += "Node OR"
        if self.type == NodeType.NOR:
            res += "Node NOR"
        return res
