from GameTreeNode import GameTreeNode,NodeType

"""
    GameTree class to evaluate a game and implement every method useful to
    generate a payoff matrix based in that game tree evaluation.
"""




class GameTree:
    """
        GameTree represents an instance of a Game tree evaluation.
    """

    def __init__(self,inp,_type=True,height=1):
        """
            type: AND-OR (True) or NOR (False)
        """
        self.input = inp
        self._type = _type
        self.height = height
        self.root = GameTree.Node()

    def _generate_algorithms(self):
        """
        Will generate every possible algorithm for this GameTree
        """
        pass

    def generate_payoff_matrix(self):
        """
            Method that will generate every
        """
        pass
