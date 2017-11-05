class NodeType(Enum):
    NOR = 1
    AND = 2
    OR = 3

class Node:
    """
        Represents a node in the GameTree.
    """
    def __init__(self,nodeType):
        """
          Children can either be a node or a number.
        """
        self.leftChild = None
        self.rightChild = None
        self.type = nodeType

    def set_right(self,node):
        self.rightChild = node

    def set_left(self,node):
        self.leftChild = node

    def evaluate(self):
        """
            This method will evaluate the 2 child and then return a tuple
            (result,score) where score is the number of leaves reached.
        """
        if self.type == NodeType.AND:
            return self._and()
        else if self.type == NodeType.OR:
            return self._or()
        else if self.type == NodeType.NOR:
            return self._nor()

    def _and(self):
        """
          AND evaluation between 2 children
        """
        score = 0
        res = True

        if type(self.leftChild) == bool:
            score += 1
            if not self.leftChild:
                res = False
        else:
            res = self.leftChild.evaluate()
            if not res[0]:
                res = False
            score += res[1]

        if res:
            if type(self.rightChild) == bool:
                score += 1
                if not self.rightChild:
                    res = False
            else:
                res = self.rightChild.evaluate()
                if not res[0]:
                    res = False
                score += res[1]

        return (res,score)

    def _or(self):
        """
            OR evaluation between 2 children
        """
        score = 0
        res = False

        if type(self.leftChild) == bool:
            score += 1
            if self.leftChild:
                res = True
        else:
            res = self.leftChild.evaluate()
            if res[0]:
                res = True
            score += res[1]

        if not res:
            if type(self.rightChild) == bool:
                score += 1
                if self.rightChild:
                    res = True
            else:
                res = self.leftChild.evaluate()
                if res[0]:
                    res = True
                score += res[1]

        return (res,score)

    def _nor(self):
        """
            OR evaluation between 2 children
        """
        score = 0
        flag = False
