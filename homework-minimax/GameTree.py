from GameTreeNode import GameTreeNode,NodeType
import itertools

"""
    GameTree class to evaluate a game and implement every method useful to
    generate a payoff matrix based in that game tree evaluation.
"""

class GameTree:
    """
        GameTree represents an instance of a Game tree evaluation.
    """
    AND_OR = [NodeType.AND,NodeType.OR]
    NOR_NOR = [NodeType.NOR,NodeType.NOR]

    def __init__(self,_type=True,height=1):
        """
            type: AND-OR (True) or NOR (False)
        """
        self._type = _type
        self.height = height
        self.nodes = []
        self._generate_tree()
        self.algorithms = []
        self.inputs = []

    def get_algorithms(self):
        return self.algorithms

    def get_inputs(self):
        return self.inputs

    def evaluate():
        return self.nodes[0].evaluate()

    def _generate_tree(self):
        """
            This method will generate the tree based on the type of GameTree.
        """
        nodes_per_level = [2**i for i in range(self.height)]
        tree_type = GameTree.AND_OR if self._type else GameTree.NOR_NOR

        lastNode = 0
        direction = False
        self.nodes.append(GameTreeNode())

        #generate tree structure
        for i in range(sum(nodes_per_level)-1):
            self.nodes.append(GameTreeNode())
            if not direction:
                self.nodes[lastNode].set_left(self.nodes[-1])
                direction = True
            else:
                self.nodes[lastNode].set_right(self.nodes[-1])
                lastNode +=1
                direction = False

        lastNode = 0
        for i in range(len(nodes_per_level)):
            node_type = tree_type[i%2]
            for j in range(nodes_per_level[i]):
                self.nodes[lastNode].set_type(node_type)
                lastNode += 1

    def hardcode(self):
        """
            Let's hardcode something
        """

        self.nodes[0].set_direction(True)
        self.nodes[1].set_direction(True)
        self.nodes[2].set_direction(True)

        self.nodes[1].set_left(False)
        self.nodes[1].set_right(True)
        self.nodes[2].set_left(True)
        self.nodes[2].set_right(True)

        print(self.nodes[0])
        print(self.nodes[1])
        print(self.nodes[2])

        return self.nodes[0].evaluate()

    def generate_payoff_matrix(self):
        """
            Method that will generate a payoff matrix for this Game Tree by
            generating every possible algorithm to evaluate it with every possible
            input from the player.
        """
        self.algorithms = [i for i in itertools.product((False,True), repeat=len(self.nodes))]
        self.inputs = [i for i in itertools.product((False,True), repeat=len(self.nodes)+1)]
        payoff_matrix = [[0 for j in range(len(self.inputs))] for i in range(len(self.algorithms))]

        dico = {}
        for i in range(len(self.algorithms)):
            for j in range(len(self.algorithms[i])):
                self.nodes[j].set_direction(self.algorithms[i][j])

            # with this algorithm, generate the cost for every input
            for j in range(len(self.inputs)):
                for k in range(len(self.inputs[j])):
                    if k%2:
                        self.nodes[len(self.nodes)//2+k//2].set_right(self.inputs[j][k])
                    else:
                        self.nodes[len(self.nodes)//2+k//2].set_left(self.inputs[j][k])
                payoff_matrix[i][j] = -self.nodes[0].evaluate()[1]

        return payoff_matrix
